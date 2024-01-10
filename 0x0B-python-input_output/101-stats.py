#!/usr/bin/python3
"""
    A log parsing script
"""
import sys


def print_data(total_size, status_codes):
    """prints the metrics parsed"""
    data = f"File size: {total_size}\n"
    sorted_status_codes = sorted(status_codes)
    for code in sorted_status_codes:
        if status_codes[code] > 0:
            data += str(code) + ': ' + str(status_codes[code]) + '\n'
    print(data, end='')


def main():
    count, total_size = 0, 0
    status_codes = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0,
        }

    try:
        for line in sys.stdin:
            count += 1
            line = line.split()[-2:]
            total_size += int(line[-1])
            code = int(line[0])
            status_codes[code] += 1
            if count % 10 == 0:
                print_data(total_size, status_codes)
    except KeyboardInterrupt:
        print_data(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
