#!/usr/bin/python3

def safe_print_integer(value):
    try:
        ret = False
        print("{:d}".format(value))
        ret = True
    except ValueError:
        pass
    finally:
        return ret
