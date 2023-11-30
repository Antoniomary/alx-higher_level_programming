#!/usr/bin/python3

"""a program that prints the number of and the list of its arguments.
"""

if __name__ == "__main__":
    import sys

    argv = sys.argv
    argc = len(argv)

    if argc - 1 == 0 or argc - 1 >= 2:
        print("{} arguments{}".format(argc - 1, ":" if argc > 1 else "."))
        if argc - 1 == 0:
            sys.exit(0)
    elif argc - 1 == 1:
        print("1 argument:")

    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))
