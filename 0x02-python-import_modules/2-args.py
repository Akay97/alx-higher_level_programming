#!/usr/bin/python3
import sys

arg = len(sys.argv) - 1
if arg == 0:
    print("0 arguments.")
elif arg == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(arg))
for num in range(arg):
    print("{}: {}".format(num + 1, sys.argv[num + 1]))
