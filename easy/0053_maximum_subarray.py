"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def maxSubArray(nums: List[int]) -> int:
    """
    참고 : https://leetcode.com/problems/maximum-subarray/discuss/20396/Easy-Python-Way
    참고2 : https://medium.com/@vdongbin/kadanes-algorithm-%EC%B9%B4%EB%8D%B0%EC%9D%B8-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-acbc8c279f29
    """
    for i in range(1, len(nums)):
        # 동일한 의미!
        # if nums[i - 1] > 0:
        #     nums[i] += nums[i - 1]
        nums[i] = max(nums[i], nums[i - 1] + nums[i])
    return max(nums)


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = maxSubArray(nums)
    print(result)
