#!/usr/bin/python3
"""modulo"""


def append_write(filename="", text=""):
    """append a string"""
    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
