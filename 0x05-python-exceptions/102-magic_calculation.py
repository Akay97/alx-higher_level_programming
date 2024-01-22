#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0

    for m in range(1, 4):
        try:
            if m > a:
                raise Exception('Too far')
            result += a ** b / m
        except Exception:
            result += b + a

    return result
