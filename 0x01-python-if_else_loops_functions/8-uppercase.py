#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        a = ord(str[i])
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            a = a - 32
        print("{}".format(chr(a)), end="")
    print("")
