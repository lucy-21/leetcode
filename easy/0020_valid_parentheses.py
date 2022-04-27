"""
Input: s = "()"
Output: true
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def isValid(s: str) -> bool:
    brackets = [bracket for bracket in s]

    bracket_map = {"{": "}", "(": ")", "[": "]"}
    stack = []
    for bracket in brackets:
        if bracket in bracket_map.keys():
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False

            temp = stack.pop()
            if bracket_map[temp] != bracket:
                return False

    return stack == []


if __name__ == "__main__":
    # s = "()"
    s = "()[]{}"
    # s = "(]"
    # s = ")"
    result = isValid(s)
    print(result)
