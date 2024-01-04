#!/usr/bin/python3
import hidden_4

string = dir(hidden_4)
for name in string:
    if name[:2] != "__":
        print(name)
