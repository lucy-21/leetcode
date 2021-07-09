# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def permute(nums: List[int]) -> List[List[int]]:
    # 1. DFS 이용
    results = []
    prev_elements = []

    def dfs(elements):
        # 리프 노드일 때 결과 추가
        if len(elements) == 0:
            results.append(
                prev_elements[:]
            )  # 결과 값을 추가하기 위해 반드시 [:] 사용!! (그냥 prev_elemetns -> 참조)

        # 순열 생성 재귀 호출
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)
            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results

    # 2. itertools 이용
    # return [list(num) for num in itertools.permutations(nums)]


if __name__ == "__main__":
    result = permute([1, 2, 3])
    print(result)
