#!/usr/bin/python3
"""modulo"""
import json


def load_from_json_file(filename):
    """create an obj"""
    with open(filename) as f:
        return json.load(f)
