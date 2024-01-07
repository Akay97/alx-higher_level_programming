#!/usr/bin/env python3

def no_c(my_string):
    string =""
    for lit in my_string:
        if lit != "c" and lit != "C":
            string += lit
    return string
