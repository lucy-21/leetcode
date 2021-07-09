# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def fib(n: int) -> int:
    dp = {}
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    result = fib(2)
    print(result)
