"""
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def climbStairs(n: int) -> int:
    """
    #1 1까지 가능한 경우의 수 = 1    (1)
    #2 2까지 가능한 경우의 수 = #1 + 1 = 2    (11, 2)
    #3 3까지 가능한 경우의 수 = #1 + #2 = 3    (111, 12, 21)
    #4 4까지 가능한 경우의 수 = #2 + #3 = 5    (1111, 112, 121, 211, 22)
    #5 5까지 가능한 경우의 수 = #3 + #4 = 8    (11111, 1112, 1121, 1211, 2111, 122, 212, 221)
    ...
    #n n까지 가능한 경우의 수 = #n-2 + #n-1
    """
    steps = [1, 2]  # 초기값 세팅 (1, 2에 대한 값)
    for i in range(2, n):
        steps.append(steps[i - 2] + steps[i - 1])
    return steps[-1] if n > 2 else steps[n - 1]


if __name__ == "__main__":
    n = 4
    result = climbStairs(n)
    print(result)
