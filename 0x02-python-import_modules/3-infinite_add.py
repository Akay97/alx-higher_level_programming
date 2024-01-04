#!/usr/bin/python3

import sys

add = 0
for num in range(len(sys.argv) - 1):
    add += int(sys.argv[num + 1])
print("{}".format(add))
