# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def twoSum(nums: List[int], target: int) -> List[int]:
    for idx1 in range(len(nums)):
        for idx2 in range(len(nums)):
            if idx1 == idx2:
                continue
            if (nums[idx1] + nums[idx2]) == target:
                return [idx1, idx2]


if __name__ == "__main__":
    result = twoSum([2, 7, 11, 15], 9)
    print(result)
