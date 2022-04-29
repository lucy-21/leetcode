"""
Input: root = [1,null,2,3]
Output: [1,3,2]
"""

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def inorder_traverse(node: Optional[TreeNode], result: List[int]) -> None:
        if not node:
            return None

        inorder_traverse(node.left, result)
        result.append(node.val)
        inorder_traverse(node.right, result)

    inorder_traverse(root, result)
    return result


if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    result = inorderTraversal(root)
    print(result)
