#!/usr/bin/python3

"""a program that prints all the names defined by the compiled
module hidden_4.pyc

please download it locally using:
curl -Lso "hidden_4.pyc" "https://github.com/alx-tools/0x02.py/raw/
master/hidden_4.pyc"

expected result:
guillaume@ubuntu:~/0x02$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
"""

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)

    for name in names:
        name_len = len(name)
        if name_len >= 2 and name[0] == '_' and name[1] == '_':
            continue
        else:
            print(name)
