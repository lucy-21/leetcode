"""
Input: head = [1,2,2,1]
Output: true
"""

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def isPalindrome(head: Optional[ListNode]) -> bool:
    """
    best solution : https://leetcode.com/problems/palindrome-linked-list/discuss/64689/Python-easy-to-understand-solution-with-comments-(operate-nodes-directly).

    1 2 3 4 4 5 6 | 6 5 4 4 3 2 1
    """
    vals = []
    while head:
        vals.append(head.val)
        head = head.next

    i = 0
    j = len(vals) - 1
    while i <= j:
        if vals[i] != vals[j]:
            return False
        i += 1
        j -= 1

    return True


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)

    result = isPalindrome(head)
    print(result)
