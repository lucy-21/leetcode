# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def combine(n: int, k: int) -> List[List[int]]:
    # 1. DFS 이용
    # results = []

    # def dfs(elements, start: int, k: int):
    #     if k == 0:
    #         results.append(elements[:])
    #         return
    #     # 자신 이전의 모든 값을 고정하여 재귀 호출
    #     for i in range(start, n + 1):
    #         elements.append(i)
    #         dfs(elements, i + 1, k - 1)
    #         elements.pop()

    # dfs([], 1, k)
    # return results

    # 2. itertools 이용
    return [list(num) for num in itertools.combinations(range(1, n + 1), k)]


if __name__ == "__main__":
    result = combine([1, 2, 3])
    print(result)
