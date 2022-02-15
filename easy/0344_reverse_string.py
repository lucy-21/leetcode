# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def reverseString(self, s: List[str]) -> None:
    s.reverse()


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    result = reverseString(s)
    print(s)
