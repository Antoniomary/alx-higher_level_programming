#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError as ZE:
        result = None
    finally:
        if result:
            print("Inside result: {:.1f}".format(result))
        else:
            print("Inside result: {}".format(result))
        return result
