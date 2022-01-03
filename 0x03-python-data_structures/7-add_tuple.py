#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, b = len(tuple_a), len(tuple_b)
    tutup1 = (tuple_a[0] if a > 0 else 0) + (tuple_b[0] if b > 0 else 0)
    tutup2 = (tuple_a[1] if a > 1 else 0) + (tuple_b[1] if b > 1 else 0)
    tutup3 = (tutup1, tutup2)
    return tutup3
