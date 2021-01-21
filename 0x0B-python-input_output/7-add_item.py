#!/usr/bin/python3
"""Defines a function to save a list of arguments to a file"""
import json
import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


try:
    plist = load("add_item.json")
except FileNotFoundError:
    plist = []
for arg in sys.argv:
    plist.append(sys.argv[arg])

save(plist, "add_item.json")
