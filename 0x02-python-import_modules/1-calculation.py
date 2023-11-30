#!/usr/bin/python3

if __name__ == "__main__":
    """a program that imports functions, does some Maths,
    and prints the result.
    """

    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    # addition operation
    print("{} + {} = {}".format(a, b, add(a, b)))

    # subtraction operation
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # multiplication operation
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # division operation
    print("{} / {} = {}".format(a, b, div(a, b)))
