"""
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Input: [1,2], [1,1]
Output: [1]
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    (low_list, high_list) = (
        (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
    )
    results = []
    for num in low_list:
        if num in high_list:
            results.append(num)
            high_list.remove(num)
    return results


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [1, 1]
    result = intersect(nums1, nums2)
    print(result)
