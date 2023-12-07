#!/usr/bin/python3

def roman_to_int(roman_string):
    """a converts a Roman numeral to an integer.

    Args:
        roman_string: the roman numeral to convert

    Returns:
        the equivalent decimal of the roman numeral else
        0 if roman_string is not a string or None.
    """
    if roman_string is None or type(roman_string) != str:
        return 0

    decimal = 0
    for char in roman_string:
        if char not in "IVXLCDM":
            return decimal

    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    for i in range(len(roman_string)):
        if i > 0 and romans[roman_string[i]] > romans[roman_string[i - 1]]:
            j = i - 1
            decimal += romans[roman_string[i]] - 2 * romans[roman_string[j]]
        else:
            decimal += romans[roman_string[i]]

    return decimal
