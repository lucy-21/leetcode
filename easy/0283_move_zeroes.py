"""
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    for _ in range(0, len(nums)):
        if nums[i] == 0:
            nums.remove(0)
            nums.append(0)
        else:
            i += 1

    return


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    print(nums)
