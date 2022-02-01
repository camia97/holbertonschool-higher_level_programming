#!/usr/bin/python3
"""modulo"""


def write_file(filename="", text=""):
    """function write"""
    with open(filename, "w+", encoding="UTF-8") as f:
        return f.write(text)
