#!/usr/bin/env python3

def no_c(my_string):
    new_string =""
    for lit in my_string:
        if lit != "c" and lit != "C":
            new_string += lit
    return new_string
