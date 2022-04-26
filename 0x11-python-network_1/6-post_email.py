#!/usr/bin/python3
"""Python Networking 1"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    myobj = {'email': sys.argv[2]}
    x = requests.post(url, data = myobj)
    print(x.text)
