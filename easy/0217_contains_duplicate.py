"""
Input: nums = [1,2,3,1]
Output: true
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def containsDuplicate(nums: List[int]) -> bool:
    return collections.Counter(nums).most_common(1)[0][1] > 1


if __name__ == "__main__":
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result = containsDuplicate(nums)
    print(result)
