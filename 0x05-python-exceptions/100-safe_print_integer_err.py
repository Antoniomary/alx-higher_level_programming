#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        err = "Unknown format code 'd' for object of type 'str'"
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: {}".format(err), file=sys.stderr)
        return False
