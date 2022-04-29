"""
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

from audioop import reverse
import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def subsets(nums: List[int]) -> List[List[int]]:
    """
    loop 돌면서
    이전 결과에 현재 숫자를 더한걸 추가
    """
    res = [[]]
    for num in nums:
        for idx in range(len(res)):
            res.append(res[idx] + [num])
    return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    # nums = [0]
    result = subsets(nums)
    print(result)
