from f5.bigip import BigIP
import logging
import os
import sys
import traceback
from f5.utils.responses.handlers import Stats
import time

# logging output format
FORMATTER = logging.Formatter('%(asctime)s [%(levelname)s] [%(threadName)s] %(message)s')

logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger("paramiko").setLevel(logging.WARNING)

# stdout logging handler
STREAM_HANDLER = logging.StreamHandler()
STREAM_HANDLER.setLevel(logging.INFO)
STREAM_HANDLER.setFormatter(FORMATTER)
logging.getLogger().addHandler(STREAM_HANDLER)

# file logging handler
LOGFILE_PATH = './update_node.log'
FILE_HANDLER = None


def set_log_file(pool_name, operation):
    global LOGFILE_PATH, FILE_HANDLER
    if operation:
        LOGFILE_PATH = './update_' + pool_name + '_' + operation + '.log'
    else:
        LOGFILE_PATH = './get_nodes_' + pool_name + '.log'
    FILE_HANDLER = logging.FileHandler(LOGFILE_PATH, mode='w')
    FILE_HANDLER.setLevel(logging.DEBUG)
    FILE_HANDLER.setFormatter(FORMATTER)
    logging.getLogger().addHandler(FILE_HANDLER)


# create custom exception hook to avoid trace-backs in stderr.
def exception_hook(ex_type, value, tb):
    logging.error("Operation failed with: {}. Please see: {} for more details."
                  .format(ex_type.__name__, os.path.normpath(os.path.join(os.getcwd(), LOGFILE_PATH))))
    msg = "".join(traceback.format_exception(ex_type, value, tb))

    with open(LOGFILE_PATH, mode='a') as f:
        f.write(msg)

sys.excepthook = exception_hook


class CarbF5(object):
    """Control class for F5 BigIp.
    Usage: carb_f5.update_odd_even_nodes(bigip, username, password, pool-name, odd-even = odd, even,
    operation = enable, disable)
    Disable: Set session of node to user-disabled (not an active node in pool)
    Enable: Set session of node to user-enabled (active node in pool)
    Odd Nodes: Hostname contains odd number, eg: cls-cvm-001, cls-cvm-007, cls-cvm-011
    Even Nodes: Hostname contains even number, eg: cls-cvm-002, cls-cvm-008, cls-cvm-012
    example: carb_f5.update_odd_even_nodes(10.10.10.10, test, test, odd, disable)"""

    def __init__(self, args):
        set_log_file(args.pool_name, args.operation)
        self.bigip_server = args.bigip_server
        self.username = args.username
        self.password = args.password
        self.pool_name = args.pool_name
        self.operation = args.operation
        self.my_partition = 'Common'
        self.odd_even = args.odd_even
        if self.operation == 'disable':
            self.session = 'user-disabled'
            self.state = 'user-down'
        elif self.operation == 'enable':
            self.session = 'user-enabled'
            self.state = 'user-up'
        else:
            logging.info('Operation not required for getting the hostnames')
            self.session = None
        self.conn = BigIP(self.bigip_server, self.username, self.password)
        self.update_pool = self.conn.ltm.pools.pool.load(partition=self.my_partition, name=self.pool_name)

    def get_node_hostnames(self):
        """Returns list of hostnames of nodes in a pool"""
        if not self.update_pool.members_s.get_collection():
            raise RuntimeError('Empty Pool: {}'.format(self.pool_name))
        node_names = []
        for member in self.update_pool.members_s.get_collection():
            logging.info('Node:' + member.name + ' Session:' + member.session + ' State:' + member.state)
            # Remove domain name if present
            hostname = member.name.split('.', 1)[0]
            node_names.append(hostname)
        return node_names

    def update_odd_even_nodes(self):
        """ Enable/Disable odd/even nodes in a pool based on the operation and odd_even flags
        To figure out if a node(cls-cvm-001) is odd or even we check if the numbers after the second -
        is odd or even"""
        check_connections = []
        for member in self.update_pool.members_s.get_collection():
            logging.info('Node:{} Session:{} State:{}'.format(member.name, member.session, member.state))
            # Remove domain name if present
            hostname = member.name.split('.', 1)[0]
            try:
                if self.odd_even == 'odd':
                    if int((hostname.split('-'))[2]) % 2 != 0 and (member.session != self.session):
                        logging.info('Hostname:{} is being {}d'.format(hostname, self.operation))
                        check_connections.append(member.name)
                        self.update_node_in_pool(member.name)
                else:
                    if int((hostname.split('-'))[2]) % 2 == 0 and (member.session != self.session):
                        logging.info('Hostname:{} is being {}d'.format(hostname, self.operation))
                        check_connections.append(member.name)
                        self.update_node_in_pool(member.name)
            except Exception:
                logging.info('Failed to update node session for pool {}'.format(self.pool_name))
                raise
        if self.operation == 'disable':
            self.check_node_connections(check_connections)

    def update_node_in_pool(self, pool_member):
        """Update session of a pool member(node). This operation is performed at the pool level
        Usage: carb_f5.update_node_in_pool(pool_member_name)
        Example: carb_f5.update_node_in_pool(cls-cvm-001.carboniteinc.com:443)"""
        update_pool_member = self.update_pool.members_s.members.load(partition=self.my_partition, name=pool_member)
        update_pool_member.session = self.session
        update_pool_member.state = self.state
        update_pool_member.description = 'modified through f5-python-SDK'
        update_pool_member.update()

    def check_node_connections(self, check_connections):
        """ Check if the number of connections in a node is 0"""
        for member in check_connections:
            node = self.conn.ltm.nodes.node.load(name=member.split(':')[0], partition='Common')
            node_stat = Stats(node.stats.load())
            logging.info('Number of current connections on node {} = {}'.format(member,
                                                                                node_stat.stat.serverside_curConns.value))
            while int(node_stat.stat.serverside_curConns.value) > 0:
                logging.info('Current Sessions of node {} is {}'.format(member, node_stat.stat.curSessions.value))
                logging.info('Current Connections of node {} is {}'.format(member,
                                                                           node_stat.stat.serverside_curConns.value))
                node = self.conn.ltm.nodes.node.load(name=member.split(':')[0], partition='Common')
                node_stat = Stats(node.stats.load())
                logging.info('Sleeping for 30secs')
                time.sleep(30)
