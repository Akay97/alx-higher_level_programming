#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for kee in sorted(a_dictionary.keys()):
        print("{}: {}".format(kee, a_dictionary[kee]))
