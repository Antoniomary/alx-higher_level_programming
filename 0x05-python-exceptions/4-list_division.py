#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    while i < list_length:
        try:
            value = int(my_list_1[i]) / int(my_list_2[i])
            new_list.append(value)
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except ValueError:
            new_list.append(0)
            print("wrong type")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            i += 1
    return new_list
