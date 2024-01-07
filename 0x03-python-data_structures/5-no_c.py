#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for lit in range(len(my_string)):
        if (my_string[lit] != 'c' and my_string[lit] != 'C'):
            string += my_string[lit]
    return string
