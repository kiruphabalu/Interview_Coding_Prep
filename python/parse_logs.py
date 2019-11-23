from collections import Counter
import csv
import re

def parse_log(filename):
    timestamps = []
    program_names = []
    with open(filename,'r') as log_file:
        for line in log_file:
            if 'fakehost' in line:
                line = line.split('fakehost')
                timestamps.append(line[0].strip(" "))
                program = line[1].split(":")
                program_day = (line[0].strip(" "))+program[0]
                program_names.append(program_day)
    print timestamps, program_names
    timestamp_count = Counter(timestamps)
    program_count = Counter(program_names)
    print timestamp_count, program_count
    fieldnames = ['minute', 'number_of_messages']
    with open('logs.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(fieldnames)
        writer.writerows(timestamp_count.items())

parse_log('messages')


def foo(id, depth=0):
    ...
    if depth == 0:
        # print without indentation
    else:
        # print with a prefix ' ' * 2 * depth
    ...
    foo(employee, depth + 1)
