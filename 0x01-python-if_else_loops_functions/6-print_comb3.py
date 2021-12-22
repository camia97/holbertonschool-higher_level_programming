#!/usr/bin/python3
for i in range(0, 10):
    for a in range(0, 10):
        if i < a:
            print("{}{}".format(i, a), end="")
            if i != 8:
                print(", ", end="")
print("")
