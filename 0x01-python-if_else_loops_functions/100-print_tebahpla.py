#!/usr/bin/python3
c = 91
while c > 65:
    if c % 2 == 0:
        c = c - 33
    else:
        c = c + 31
    print("{}".format(chr(c)), end="")
