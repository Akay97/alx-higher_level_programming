#!/usr/bin/python3
"""
A script that adds all command-line arguments to a Python list and then saves them to a file.

The list is saved as a JSON representation in a file named add_item.json.
"""


import sys
from json_loader import load_from_json_file
from json_saver import save_to_json_file

"""
Load existing list from file or create a new one if file doesn't exist
"""
try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []

"""
Append command line arguments to the list
"""
for arg in sys.argv[1:]:
    my_list.append(arg)

"""
Save the updated list to the file
"""
save_to_json_file(my_list, "add_item.json")
