"""
Input: x = 4
Output: 2
square_root : 제곱근, 제곱하여 그 수가 되는 수
"""

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def mySqrt(x: int) -> int:
    """
    참고 : https://leetcode.com/problems/sqrtx/discuss/25061/Python-binary-search-solution-(O(lgn)).
    """
    l, r = 0, x
    while l < r:
        mid = (l + r) // 2
        if x < mid * mid:
            r = mid
        else:
            l = mid + 1
    return l - 1 if l > 1 else l  # careful about 0,1 cases


if __name__ == "__main__":
    x = 4
    result = mySqrt(x)
    print(result)
