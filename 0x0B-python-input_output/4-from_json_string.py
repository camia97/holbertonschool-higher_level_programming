#!/usr/bin/python3
"""modulo"""
import json


def from_json_string(my_str):
    """returns an obj represented by json"""
    return json.loads(my_str)
