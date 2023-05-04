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
    ops = 0
    min_ops = 2
    while n > 1:
        while n % min_ops == 0:
            ops += min_ops
            n //= min_ops
        min_ops += 1
    return ops
