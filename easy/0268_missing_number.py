"""
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def missingNumber(nums: List[int]) -> int:
    target_sum, current_sum = 0, 0
    for i in range(len(nums)):
        target_sum += i + 1  # 1 ~ len(nums)
        current_sum += nums[i]
    return target_sum - current_sum


if __name__ == "__main__":
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    result = missingNumber(nums)
    print(result)
