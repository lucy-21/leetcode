"""
Input: m = 3, n = 7
Output: 28
"""

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def uniquePaths(m: int, n: int) -> int:
    """
    아래 또는 오른쪽 밖에 못감!

    best solution : https://leetcode.com/problems/unique-paths/discuss/1581998/C%2B%2BPython-5-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP-to-Math

    문제 -> 한번 계산한 지점을 또 계산하는게 문제
    DP Memoization -> cache 사용하면 해결됨
    """

    @functools.lru_cache
    def dfs(i, j):
        if i >= m or j >= n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1
        return dfs(i + 1, j) + dfs(i, j + 1)

    return dfs(0, 0)


if __name__ == "__main__":
    m, n = 3, 7
    # m, n = 23, 12
    result = uniquePaths(m, n)
    print(result)
