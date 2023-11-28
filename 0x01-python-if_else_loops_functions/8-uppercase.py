#!/usr/bin/python3

def uppercase(str):
    if str:
        for character in str:
            ascii_code = ord(character)
            if ascii_code >= 97 and ascii_code <= 122:
                print(chr(ascii_code - 32), end='')
            else:
                print(character, end='')
        print()
