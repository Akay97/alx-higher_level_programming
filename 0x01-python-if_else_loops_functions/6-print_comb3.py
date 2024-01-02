#!/usr/bin/python3

for num in range(9):
    for num1 in range(num+1, 10):
        if num < 8 or num1 < 9:
            print("{:d}{:d}".format(num, num1), end=", ")
        else:
            print("{:d}{:d}".format(num, num1), end="\n")
