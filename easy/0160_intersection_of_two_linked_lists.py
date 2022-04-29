"""
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
"""

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    best solution : https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/1092898/JS-Python-Java-C%2B%2B-or-Easy-O(1)-Extra-Space-Solution-w-Visual-Explanation
    """
    nodes = {}
    while headA:
        nodes[headA] = 0
        headA = headA.next
    while headB:
        if headB in nodes:
            return headB
        headB = headB.next
    return None


if __name__ == "__main__":
    inter = ListNode(8)
    inter.next = ListNode(4)
    inter.next.next = ListNode(5)

    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = inter

    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next = ListNode(1)
    headB.next = inter

    # headA = ListNode(1)
    # headB = headA

    result = getIntersectionNode(headA, headB)
    print(result)
