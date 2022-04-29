"""
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
"""

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    """
    1) root 찾기 (가운데 idx)
    2) 왼쪽, 오른쪽 list에 대해 tree 만들기
    """
    if len(nums) == 0:
        return None
    root_idx = len(nums) // 2
    return TreeNode(
        nums[root_idx],
        sortedArrayToBST(nums[:root_idx]),
        sortedArrayToBST(nums[root_idx + 1 :]),  # python은 없는 범위 입력하면 [] 반환
    )


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    result = sortedArrayToBST(nums)
    print(result)
