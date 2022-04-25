#!/usr/bin/python3
"""Python networking 1"""
import sys
import urllib.request


if __name__ == "__main__":
    if sys.argv[1] is not None:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.headers.get('X-Request-Id'))
