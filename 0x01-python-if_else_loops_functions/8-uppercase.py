#!/usr/bin/python3

def uppercase(str):
    if str:
        for char in str:
            if char >= 'a' and char <= 'z':
                char = chr(ord(char) - 32)
            print(char, end='')
        print()
