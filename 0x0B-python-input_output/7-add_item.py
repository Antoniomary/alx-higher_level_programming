#!/usr/bin/python3
"""
    A module for saving data in a list
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
retrived_data = []
try:
    retrived_data = load_from_json_file(filename)
except Exception:
    save_to_json_file([], filename)

my_list = []
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

new_data = retrived_data + my_list

save_to_json_file(new_data, filename)
