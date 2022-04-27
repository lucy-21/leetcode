"""
Input: nums = [2,2,1]
Output: 2
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def majorityElement(nums: List[int]) -> int:
    """
    과반수 이상 등장하는 수 찾기
    """
    c = collections.Counter(nums)
    return c.most_common(1)[0][0]


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    result = majorityElement(nums)
    print(result)
