#!/usr/bin/python3
"""load from json function"""

import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""

    with open(filename, "w", encoding="utf-8") as f:
        return json.load(f)
