"""
Input: haystack = "hello", needle = "ll"
Output: 2
"""

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


if __name__ == "__main__":
    haystack = "hello"
    needle = ""  # "ll"
    result = strStr(haystack, needle)
    print(result)
