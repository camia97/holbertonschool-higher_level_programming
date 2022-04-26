#!/usr/bin/python3
"""Python networking 1"""
import sys
from urllib import request, parse


if __name__ == "__main__":
    d = {"email": sys.argv[2]}
    data = parse.urlencode(d).encode()
    req = request.Request(sys.argv[1], data=data)
    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
