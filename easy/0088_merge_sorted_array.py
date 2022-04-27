"""
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.

    1 2 3 0 0 0 <- 2
    1 2 2 3 0 0 0 <- 5
    1 2 2 3 5 0 0 0 <- 6
    1 2 2 3 5 6 0 0 0
    1 2 2 3 5 6

    best solution 참고 : https://leetcode.com/problems/merge-sorted-array/discuss/29503/Beautiful-Python-Solution
    """
    if n == 0:
        return None

    idx1, idx2 = 0, 0
    while idx1 < (m + n) and idx2 < n:
        if len(nums1) == 0 or nums2[idx2] <= nums1[idx1]:  # nums1[idx1] == 0
            nums1.insert(idx1, nums2[idx2])
            del nums1[-1]
            idx2 += 1
        idx1 += 1

    while idx2 < n:
        nums1.insert(m + idx2, nums2[idx2])
        del nums1[-1]
        idx2 += 1

    return None


if __name__ == "__main__":
    # (1)
    # nums1 = [1, 2, 3, 0, 0, 0]
    # m = 3
    # nums2 = [2, 5, 6]
    # n = 3
    # (2)
    # nums1 = [2, 0]
    # m = 1
    # nums2 = [1]
    # n = 1
    # (3)
    nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    m = 6
    nums2 = [1, 2, 2]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)
