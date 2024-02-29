#!/usr/bin/python3
"""the make change interview solution"""


def makeChange(coins, total):
    """make change method"""
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[total] == float('inf') else dp[total]
