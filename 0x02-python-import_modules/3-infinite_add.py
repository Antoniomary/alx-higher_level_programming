#!/usr/bin/python3

""" a program that prints the result of the addition of all arguments
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10
89
"""

import sys

av = sys.argv
ac = len(av)

if ac == 1:
    print("0")
else:
    for i in range(1, ac):
        j = 0
        arg_len = len(av[i])
        while j < arg_len:
            if not av[i][j].isdigit():
                if j != 0 or av[i][j] not in "+-":
                    print("Error")
                    sys.exit(1)
            j += 1

    sum = 0
    for i in range(1, ac):
        sum += int(av[i])

    print(sum)
