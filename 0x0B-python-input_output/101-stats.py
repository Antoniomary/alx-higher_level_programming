#!/usr/bin/python3
"""
    A log parsing script
"""
import sys
import random


count, total_size = 0, 0
parsed_log = {}
try:
    for line in sys.stdin:
        count += 1
        line = line.split()[-2:]
        total_size += int(line[-1])
        if parsed_log.get(line[0], "Not found") == "Not found":
            parsed_log[line[0]] = 1
        else:
            parsed_log[line[0]] += 1
        if count == 10:
            print("File size: {:d}".format(total_size))
            for code in sorted(parsed_log):
                print("{:s}: {:d}".format(code, parsed_log[code]))
            count = 0
except KeyboardInterrupt:
    print("File size: {:d}".format(total_size))
    for code in sorted(parsed_log):
        print("{:s}: {:d}".format(code, parsed_log[code]))
    raise
