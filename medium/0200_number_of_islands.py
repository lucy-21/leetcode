# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def numIslands(grid: List[List[str]]) -> int:
    def dfs(i, j):
        # 더 이상 육지가 아닌 경우 종료
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return
        # 방문한 곳 마킹 (1이 아닌 무엇이든 상관없음)
        grid[i][j] = 0
        # 동서남북 탐색
        dfs(i + 1, j)  # 동
        dfs(i - 1, j)  # 서
        dfs(i, j + 1)  # 남
        dfs(i, j - 1)  # 북

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(i, j)
                # 모든 육지 탐색 후 카운트 1 증가
                count += 1

    return count


if __name__ == "__main__":
    input_data = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    result = numIslands(input_data)
    print(result)
