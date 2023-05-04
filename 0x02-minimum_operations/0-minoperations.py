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
    """If n == 1, then the answer is 1."""
    if n == 1:
        return 1

    """Create a dp array that stores the minimum number
    of operations needed to result in exactly i H
    characters in the file.
    The dp array is initialized with the following values:
    dp[1] = 1
    dp[i] = 0 for i > 1"""
    
    dp = [0] * (n + 1)
    dp[1] = 1

    """Iterate through the dp array, starting at index 2.
    For each index i, calculate the minimum number of operations
    needed to result in exactly i H characters in the file.
    The minimum number of operations is calculated as follows:
    If i is even, then the minimum number of operations is 1 + dp[i // 2].
    If i is odd, then the minimum number of operations is 1 + dp[i - 1]."""
    
    for i in range(2, n + 1):
        dp[i] = 1 + min(dp[i - 1], dp[i // 2])

    """Return the value of dp[n]."""
    return dp[n]
