#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5
    c = calc.add(a, b)
    print("{} + {} = {}".format(a, b, c))
    s = calc.sub(a, b)
    print("{} - {} = {}".format(a, b, s))
    m = calc.mul(a, b)
    print("{} * {} = {}".format(a, b, m))
    d = calc.div(a, b)
    print("{} / {} = {:.0f}".format(a, b, d))
