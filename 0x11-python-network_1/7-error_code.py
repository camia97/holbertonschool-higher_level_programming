#!/usr/bin/python3
"""Python Networking 1"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code == 200:
        print('Index')
    else:
        print('Error code: {}'.format(r.status_code))
