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
    operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            operations += min_operations
            n /= min_operations
        min_operations += 1
    return operations
