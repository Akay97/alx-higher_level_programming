#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    na_tuple = tuple_a[0] if len(tuple_a) > 0 else 0
    nb_tuple = tuple_a[1] if len(tuple_a) > 1 else 0

    na_tuple += tuple_b[0] if len(tuple_b) > 0 else 0
    nb_tuple += tuple_b[1] if len(tuple_b) > 1 else 0

    return na_tuple, nb_tuple
