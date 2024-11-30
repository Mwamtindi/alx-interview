#!/usr/bin/python3
"""
Determines the fewest num of coins needed to meet a given total
"""


def makeChange(coins, total):
    """
    Determines fewest num of coins needed to meet the given total

    Args:
        coins (list): List of values of the coins.
        total (int): The target amount.

    Returns:
        int: Fewest num of coins needed, or -1 if ttl cannt be met
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin

    return count if total == 0 else -1
