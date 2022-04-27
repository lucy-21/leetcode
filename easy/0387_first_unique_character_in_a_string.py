"""
Input: s = "leetcode"
Output: 0
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def firstUniqChar(s: str) -> int:
    counts = {}
    for idx, char in enumerate(s):
        if char not in counts:
            counts[char] = idx
        else:
            counts[char] = 999999
    first_uniq_idx = sorted(list(counts.values()))[0]
    return first_uniq_idx if first_uniq_idx != 999999 else -1


if __name__ == "__main__":
    s = "aabb"
    result = firstUniqChar(s)
    print(result)
