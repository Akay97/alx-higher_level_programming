#!/usr/bin/python3
def uppercase(str):
    for c in str:
        uppercase_char = chr(ord(c) - 32) if 'a' <= c <= 'z' else c
        print("{}".format(uppercase_char), end="")
    print()
