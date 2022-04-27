"""
Input: n = 27
Output: true
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def isPowerOfThree(n: int) -> bool:
    temp_n = n
    while temp_n >= 3:
        if temp_n % 3 == 0:
            temp_n = temp_n // 3
        else:
            return False

    return temp_n == 1


if __name__ == "__main__":
    n = 0
    result = isPowerOfThree(n)
    print(result)
