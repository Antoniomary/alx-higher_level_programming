#!/usr/bin/python3

if __name__ == "__main__":
    """a program that imports functions, does some Maths,
    and prints the result.
    """

    import calculator_1 as calc

    a = 10
    b = 5

    # addition operation
    print("{} + {} = {}".format(a, b, calc.add(a, b)))

    # subtraction operation
    print("{} - {} = {}".format(a, b, calc.sub(a, b)))

    # multiplication operation
    print("{} * {} = {}".format(a, b, calc.mul(a, b)))

    # division operation
    print("{} / {} = {}".format(a, b, calc.div(a, b)))
