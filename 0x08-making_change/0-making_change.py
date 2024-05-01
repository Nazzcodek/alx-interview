#!/usr/bin/python3
"""this module determine the number of coin to make change"""


def makeChange(coins, total):
    """this methode get the number of coin to get total"""
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
