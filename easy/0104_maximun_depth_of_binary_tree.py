"""
Input: root = [3,9,20,null,null,15,7]
Output: 3
"""

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    def traverse(node: Optional[TreeNode], depth: int) -> int:
        if node:
            return max(traverse(node.left, depth + 1), traverse(node.right, depth + 1))
        else:
            return depth - 1

    return traverse(root, 1)


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    result = maxDepth(root)
    print(result)
