"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def maxProfit(prices: List[int]) -> int:
    """
    [7 1 5 3 6 4]
    (fail case)
     0
     - 5
     - - 5         1 vs 5
     - - - 5       3 vs 5
     - - - - 5
     - - - - - 5
    현재값 = max(직전까지의 최대값, 내가 얻을 수 있는 최대값)

    (success case)
    현재까지 제일 작았던 수를 기억 = n
    - n보다 크면 profit 계산 -> max_profit 기억
    - n보다 작으면 n 값 변경
    """
    # fail case - time out
    # max_profit = 0
    # for i in range(len(prices) - 1):
    #     for j in range(i + 1, len(prices)):
    #         max_profit = max(max_profit, prices[j] - prices[i])

    max_profit = 0
    min_price = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            max_profit = max(max_profit, prices[i] - min_price)
    return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    result = maxProfit(prices)
    print(result)
