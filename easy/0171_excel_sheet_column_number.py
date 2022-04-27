"""
Input: columnTitle = "A"
Output: 1
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def titleToNumber(columnTitle: str) -> int:
    """
    A -> 1
    B -> 2
    C -> 3
    ...
    Y -> 25
    Z -> 26
    AA -> 27 (앞 A = 26)
    AB -> 28
    ...
    AZ -> 52
    BA -> 53 (앞 B = 52)
    BB -> 54

    ** 각 자리수 별 값 = 26 * 자리수 * 해당 알파벳 값
    ** 최종 합 = SUM(각 자리수 별 값)

    ex)
    ZY = (26 * 1 * 26) + 25 = 676 + 25 = 701


    아스키 코드 값
    A 65
    """
    ret = 0
    for idx, alpha in enumerate(columnTitle):
        ret += pow(26, (len(columnTitle) - idx - 1)) * (ord(alpha) - ord("A") + 1)
    return ret


if __name__ == "__main__":
    columnTitle = "ZY"
    result = titleToNumber(columnTitle)
    print(result)
