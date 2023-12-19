#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        err = "Exception: Unknown format code 'd' for object of type 'str'\n"
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        sys.stderr.write(err)
        return False
