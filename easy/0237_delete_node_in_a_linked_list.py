"""
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
"""

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(node: ListNode) -> None:
    node.val = node.next.val
    node.next = node.next.next
    return None


if __name__ == "__main__":
    node = ListNode(4)
    target = ListNode(5)
    node.next = target
    node.next.next = ListNode(1)
    node.next.next.next = ListNode(9)

    result = deleteNode(node)
    print(result)
