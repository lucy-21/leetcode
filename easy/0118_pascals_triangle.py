"""
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def generate(numRows: int) -> List[List[int]]:
    """
    #0  0 1 0
    #1  0 1 1 0
    #2  0 1 2 1 0
    #3  0 1 3 3 1 0
    """
    pascal_triangle = [[1]]

    for idx in range(numRows - 1):
        current_row = [0] + pascal_triangle[idx] + [0]
        next_row = [
            current_row[i - 1] + current_row[i] for i in range(1, len(current_row))
        ]
        pascal_triangle.append(next_row)

    return pascal_triangle


if __name__ == "__main__":
    numRows = 5
    result = generate(numRows)
    print(result)
