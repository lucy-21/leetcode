"""
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def plusOne(digits: List[int]) -> List[int]:
    if digits[-1] == 9:
        idx = -1
        while abs(idx) <= len(digits) and digits[idx] == 9:
            digits[idx] = 0
            idx -= 1

        if abs(idx) > len(digits):
            digits = [1] + digits
        else:
            digits[idx] += 1
    else:
        digits[-1] += 1
    return digits


if __name__ == "__main__":
    # digits = [1, 2, 3]
    # digits = [4, 3, 2, 1]
    # digits = [9]
    # digits = [9, 9]
    digits = [8, 9, 9, 9]
    result = plusOne(digits)
    print(result)
