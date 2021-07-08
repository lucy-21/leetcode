# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def isPalindrome(s: str) -> bool:
    chars = [c for c in s.lower() if c.isalnum()]
    return chars == chars[::-1]


if __name__ == "__main__":
    result = isPalindrome("0P")  # A man, a plan, a canal: Panama
    print(result)
