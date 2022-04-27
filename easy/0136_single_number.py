"""
Input: nums = [2,2,1]
Output: 1
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def singleNumber(nums: List[int]) -> int:
    """
    XOR : 두 가지의 조건이 서로 반대의 값을 가지면, 결과가 참

    1 0 1
    0 1 1
    -----
    0 0 1 AND
    1 1 1 OR
    1 1 0 XOR

    (같은 수일 경우) -> 무조건 0이 나옴
    1 1 1
    1 1 1
    -----
    0 0 0 XOR

    1개 빼고 나머진 전부 같은 숫자의 쌍 -> 모든 숫자를 XOR하면 1개만 남음
    """
    # return collections.Counter(nums).elements()[-1]
    xor = 0
    for num in nums:
        xor ^= num
    return xor


if __name__ == "__main__":
    nums = [2, 2, 1]
    result = singleNumber(nums)
    print(result)
