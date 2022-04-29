"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def maxArea(height: List[int]) -> int:
    """
    best solution 참고 : https://leetcode.com/problems/container-with-most-water/discuss/1915108/Python3-GREEDY-TWO-POINTERS-~(~)-Explained
    """
    max_area = 0
    left_idx, right_idx = 0, len(height) - 1
    while left_idx < right_idx:
        max_area = max(
            max_area, (right_idx - left_idx) * min(height[left_idx], height[right_idx])
        )
        if height[left_idx] < height[right_idx]:
            left_idx += 1
        else:
            right_idx -= 1
    return max_area


if __name__ == "__main__":
    # height = [1, 8, 6, 2, 5, 4, 9, 3, 7]  # result = 49
    # height = [1, 1]
    # height = [1, 2, 1]
    height = [1, 2, 4, 3]
    result = maxArea(height)
    print(result)
