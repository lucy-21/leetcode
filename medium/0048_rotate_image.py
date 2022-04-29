"""
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

from audioop import reverse
import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def pprint(matrix: List[List[int]]) -> None:
    for row in matrix:
        print(row)
    print("\n")
    return


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.

    best solution : https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)
    """
    n = len(matrix)
    diff = n - 1
    middle = n // 2
    for i in range(middle):
        for j in range(i, diff - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[diff - j][i]
            matrix[diff - j][i] = matrix[diff - i][diff - j]
            matrix[diff - i][diff - j] = matrix[j][diff - i]
            matrix[j][diff - i] = temp
    return None


if __name__ == "__main__":
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(matrix)
    pprint(matrix)
