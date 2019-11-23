class Solution:
    # @param gas : tuple of integers
    # @param cost : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        res = 0
        cur_gas = 0
        for i in xrange(len(gas)):
            cur_gas += gas[i] - cost[i]
            if cur_gas < 0:
                cur_gas = 0
                res = i + 1
        return res
