"""
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def longestCommonPrefix(strs: List[str]) -> str:
    min_length = min([len(st) for st in strs])

    longest_prefix = ""
    for i in range(0, min_length):
        chars = [st[i : i + 1] for st in strs]
        chars = list(set(chars))
        if len(chars) > 1:
            break
        else:
            longest_prefix = longest_prefix + chars[0]
    return longest_prefix


if __name__ == "__main__":
    # strs = ["flower", "flow", "flight"]
    strs = ["dog", "racecar", "car"]
    result = longestCommonPrefix(strs)
    print(result)
