#!/usr/bin/python3
"""
Make change module
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine fewest number of coins
    needed to meet a given amount 'total'

    Args:
        coins (list): a list of values of coins in your possession
        total (number): target amount

    Returns:
        int: fewest number of coins needed to meet total
             or -1 if total cannot be reached

    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order

    i, ncoins = (0, 0)  # Initialize variables for iteration and coin count
    cpy_total = total  # Make a copy of total amount
    len_coins = len(coins)  # Get length of coins list

    # Iterate over coins and decrement total amount
    while i < len_coins and cpy_total > 0:
        if (cpy_total - coins[i]) >= 0:  # Check if current coin can be used
            cpy_total -= coins[i]  # Deduct coin value from total amount
            ncoins += 1  # Increment coin count
        else:
            i += 1  # Move to next coin if current coin is too large

    # Check if total amount is not fully covered or no coins were used
    check = cpy_total > 0 and ncoins > 0
    return -1 if check or ncoins == 0 else ncoins  # Return -1 or no of coins
