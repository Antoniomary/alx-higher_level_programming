#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        err = "Exception: Unknown format code 'd' for object of type 'str'\n"
        ret = False
        print("{:d}".format(value))
        ret = True
    except (ValueError, TypeError):
        sys.stderr.write(err)
    finally:
        return ret
