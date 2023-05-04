#!/usr/bin/python3
"""
This function calculates the fewest number of operations
needed to result in exactly n H characters in the file.

Parameters
----------
n : int
    The number of H characters to be in the file.

Returns
-------
int
    The fewest number of operations needed to result
    in exactly n H characters in the file.
"""

def minOperations(n):
    if n <= 1:
        return n

    num_ops = 0
    num_h = 1
    buffer = 0

    while num_h < n:
        if n % num_h == 0:
            buffer = num_h
        num_h += buffer
        num_ops += 1

    return num_ops