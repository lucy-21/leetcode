"""
Input: root = [1,2,2,3,4,4,3]
Output: true
"""

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:
    """
    각 가지에 대해,
    node의 left vs node의 right 비교
    """

    def traverse(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> None:
        if node1 == None or node2 == None:
            return node1 == None and node2 == None

        if node1 and node2:
            if node1.val != node2.val:
                return False
            if not traverse(node1.left, node2.right):
                return False
            if not traverse(node1.right, node2.left):
                return False
        return True

    return traverse(root.left, root.right)


if __name__ == "__main__":
    root = TreeNode(
        1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))
    )
    # root = TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(2, TreeNode(2)))
    result = isSymmetric(root)
    print(result)
