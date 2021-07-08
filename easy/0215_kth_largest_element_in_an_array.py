# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def findKthLargest(nums: List[int], k: int) -> int:
    # 1. heapq 모듈의 heapify 이용 -> 주어진 자료구조가 힙 특성을 만족하도록 바꿔줌
    # heapq.heapify(nums)
    # for _ in range(len(nums) - k):
    #     heapq.heappop(nums)
    # return heapq.heappop(nums)

    # 2. heapq 모듈의 nlargest 이용 -> n번째 큰 값까지 리스트로 추출
    # return heapq.nlargest(k, nums)[-1]

    # 3. 정렬 이용 -> 가장 빠름 (timsort 사용하여 C로 정교하게 구현되어 있기 때문)
    nums.sort()
    return nums[-k]


if __name__ == "__main__":
    result = findKthLargest([3, 2, 1, 5, 6, 4], 2)
    print(result)
