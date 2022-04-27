"""
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def reverseBits(n: int) -> int:
    # bit manipulation solution : https://leetcode.com/problems/reverse-bits/discuss/54748/AC-Python-44-ms-solution-bit-manipulation
    ans = 0
    for i in range(32):
        ans = (ans << 1) + (n & 1)
        n >>= 1
    return ans


if __name__ == "__main__":
    n = 0b00000010100101000001111010011100
    result = reverseBits(n)
    print(result)
