#!/usr/bin/python3

"""a program that imports functions from the file
calculator_1.py, does some Maths, and prints the result.
"""

if __name__ == "__main__":
    import calculator_1 as calc

    a = 10
    b = 5

    # addition operation
    result = calc.add(a, b)
    print("{} + {} = {}".format(a, b, result))

    # subtraction operation
    result = calc.sub(a, b)
    print("{} - {} = {}".format(a, b, result))

    # multiplication operation
    result = calc.mul(a, b)
    print("{} * {} = {}".format(a, b, result))

    # division operation
    result = calc.div(a, b)
    print("{} / {} = {}".format(a, b, result))
