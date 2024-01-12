#!/usr/bin/python3
"""
    A log parsing script
"""
import sys


def print_data(total_size, status_codes):
    """prints the metrics parsed"""
    res = f"File size: {total_size}\n"
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            res += str(code) + ': ' + str(status_codes[code]) + '\n'
    print(res, end='')


count, total_size = 0, 0
status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0,
    }

try:
    for line in sys.stdin:
        count += 1
        line = line.split()[-2:]
        try:
            total_size += int(line[-1])
            code = int(line[0])
            status_codes[code] += 1
        except ValueError:
            pass
        if count % 10 == 0:
            print_data(total_size, status_codes)
finally:
    print_data(total_size, status_codes)
