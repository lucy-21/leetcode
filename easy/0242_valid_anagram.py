"""
Input: s = "anagram", t = "nagaram"
Output: true
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def isAnagram(s: str, t: str) -> bool:
    # return sorted(s) == sorted(t) # more slow
    return collections.Counter(s) == collections.Counter(t)


if __name__ == "__main__":
    s = "tac"
    t = "cat"
    result = isAnagram(s, t)
    print(result)
