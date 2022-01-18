#!/usr/bin/python3
def safe_print_division(a, b):
    div = 0
    try:
        div = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {:.2f}".format(div))
    return div
