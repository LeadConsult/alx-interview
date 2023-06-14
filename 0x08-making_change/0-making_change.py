#!/usr/bin/python3
"""
Make change module
"""

def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins
    needed to meet a given amount 'total'

    Args:
        coins (list): a list of the values of the coins in your possession
        total (number): the target amount

    Returns:
        int: the fewest number of coins needed to meet the total
             or -1 if the total cannot be reached

    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort the coins in descending order

    i, ncoins = (0, 0)  # Initialize variables for iteration and coin count
    cpy_total = total  # Make a copy of the total amount
    len_coins = len(coins)  # Get the length of the coins list

    # Iterate over the coins and decrement the total amount
    while i < len_coins and cpy_total > 0:
        if (cpy_total - coins[i]) >= 0:  # Check if the current coin can be used
            cpy_total -= coins[i]  # Deduct the coin value from the total amount
            ncoins += 1  # Increment the coin count
        else:
            i += 1  # Move to the next coin if the current coin is too large

    # Check if the total amount is not fully covered or no coins were used
    check = cpy_total > 0 and ncoins > 0
    return -1 if check or ncoins == 0 else ncoins  # Return -1 or the number of coins
