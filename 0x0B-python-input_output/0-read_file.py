#!/usr/bin/python3
"""modulo"""


def read_file(filename=""):
    """open file"""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
