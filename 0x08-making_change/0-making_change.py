#!/usr/bin/python3

def makeChange(coins, total):
    """
    Calculates the minimum number of coins needed to make the given total amount.

    Args:
        coins (list): List of coin denominations.
        total (int): The total amount to be made.

    Returns:
        int: The minimum number of coins needed, or -1 if the total cannot be made.

    """
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)

    change = 0

    for coin in coins:
        if total <= 0:
            break

        # Calculate the maximum number of current coin denomination
        # that can be used
        temp = total // coin  
        change += temp  # Add the number of coins used to the total change
        # Deduct the total value of coins used from the total amount
        total -= (temp * coin)

    if total != 0:
        return -1  
    # If there is remaining amount,
    # return -1 indicating the total cannot be made

    return change
    # Return the minimum number of coins needed
