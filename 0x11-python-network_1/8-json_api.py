#!/usr/bin/python3
"""Python Networking 1"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        my_dict = {'q': sys.argv[1]}
        r = requests.post('http://0.0.0.0:5000/search_user', data=my_dict)
        try:
            print('[{}] {}'.format(r.json()['id'], r.json()['name']))
        except KeyError:
            print('No result')
        except ValueError:
            print('Not a valid JSON')
    else:
        my_dict = {'q': ""}
        print('No result')
