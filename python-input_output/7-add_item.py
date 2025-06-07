#!/usr/bin/python3
"""Script to add arguments to a list and save in a JSON file"""

import sys
import os
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"


if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []


items.extend(sys.argv[1:])


save_to_json_file(items, filename)
