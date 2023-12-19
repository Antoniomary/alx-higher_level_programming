#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    while i < list_length:
        try:
            value = int(my_list_1[i]) / int(my_list_2[i])
            new_list.append(value)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except ValueError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        i += 1
    return new_list
