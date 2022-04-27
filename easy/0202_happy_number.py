"""
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def isHappy(n: int) -> bool:
    """
    loop 탈출 조건 : 계산 결과가 기존에 나왔던 수에 포함됨 (= 무한 loop)

    n = 2 (x)
    4 !!!
    16
    1 + 36 = 37
    9 + 49 = 58
    25 + 64 = 89
    64 + 81 = 145
    1 + 16 + 25 = 42
    16 + 4 = 20
    4

    n = 3 (x)
    9
    81
    64 + 1 = 65
    36 + 25 = 61
    36 + 1 = 37 !!!
    9 + 49 = 58

    n = 4 (x) loop

    n = 7 (o)
    7^2 = 49
    16 + 81 = 97
    81 + 49 = 130
    1 + 9 = 10
    1

    n = 11 (x)
    1 + 1 = 2
    """
    temp_values, temp_result = {}, n
    while True:
        exp = [int(i) ** 2 for i in str(temp_result)]
        temp_result = sum(exp)
        if temp_result in temp_values or temp_result == 1:
            break
        temp_values[temp_result] = 0
    return temp_result == 1


if __name__ == "__main__":
    n = 7
    result = isHappy(n)
    print(result)
