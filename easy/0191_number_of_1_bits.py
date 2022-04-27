"""
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def hammingWeight(n: int) -> int:
    # bit manipulation solution : https://leetcode.com/problems/number-of-1-bits/discuss/55106/Python-2-solutions.-One-naive-solution-with-built-in-functions.-One-trick-with-bit-operation
    # c = 0
    # while n:
    #     n &= n - 1
    #     c += 1
    # return c
    return bin(n).count("1")


if __name__ == "__main__":
    n = 0b00000000000000000000000000001011
    result = hammingWeight(n)
    print(result)
