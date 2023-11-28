#!/usr/bin/python3

# use python ascii code numbers for lowercase alphabets

for n in range(97, 123):
    if n != 101 and n != 113:
        print(chr(n).format(), end='')
#        print("{:c}".format(n), end='')
