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
        return 0

    operations = 0
    for i in range(2, n+1):
        while n % i == 0:
            operations += i
            n /= i
    return operations
