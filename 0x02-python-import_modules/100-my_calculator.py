#!/usr/bin/python3

"""a calculator program that can add, substract, multiply and divide"""

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    ac = len(sys.argv)
    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    av = sys.argv
    for i in range(1, ac):
        err = "Unknown operator. Available operators: +, -, * and /"
        j = 0
        for char in av[i][j]:
            if i == 2:
                if j != 0:
                    print("Error")
                    sys.exit(1)
                elif av[i][j] not in "+-*/":
                    print(err)
                    sys.exit(1)
            elif not av[i][j].isdigit():
                if j != 0 or av[i][j] not in "+-":
                    print("Error")
                    sys.exit(1)

    a = int(av[1])
    op = av[2]
    b = int(av[3])

    if op == "/" and b == 0:
        print("Error: Can't divide by Zero")
        sys.exit(1)

    print("{} {} {}".format(a, op, b), end=' = ')
    if op == "+":
        print(add(a, b))
    elif op == "-":
        print(sub(a, b))
    elif op == "*":
        print(mul(a, b))
    elif op == "/":
        print(div(a, b))
