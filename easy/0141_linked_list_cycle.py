"""
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    """
    python fast solution : https://leetcode.com/problems/linked-list-cycle/discuss/44494/Except-ionally-fast-Python
    """
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False


if __name__ == "__main__":
    head = ListNode(3)
    pos = ListNode(2)
    head.next = pos
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = pos

    result = hasCycle(head)
    print(result)
