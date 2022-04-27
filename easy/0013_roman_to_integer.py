"""
Input: s = "III"
Output: 3
Explanation: III = 3.
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def romanToInt(s: str) -> int:
    symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    results = []
    idx = 0
    while idx < len(s):
        if idx < len(s) - 1 and symbols[s[idx]] < symbols[s[idx + 1]]:
            results.append(symbols[s[idx + 1]] - symbols[s[idx]])
            idx += 1
        else:
            results.append(symbols[s[idx]])
        idx += 1
    return sum(results)


if __name__ == "__main__":
    s = "MCMXCIV"
    result = romanToInt(s)
    print(result)
