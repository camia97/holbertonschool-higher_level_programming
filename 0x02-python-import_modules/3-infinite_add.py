#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0")
    else:
        suma = 0
        for i in range(1, len(sys.argv)):
            a = int(sys.argv[i])
            suma = int(sys.argv[i]) + suma
        print(suma)
