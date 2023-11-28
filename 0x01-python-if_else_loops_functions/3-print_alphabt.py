#!/usr/bin/python3

# use python ascii code numbers for lowercase alphabets
for ascii in range(97, 123):
    if chr(ascii) not in 'qe':
        # print one alphabet at a time and remove auto-newline
        print("{}".format(chr(ascii)), end='')
