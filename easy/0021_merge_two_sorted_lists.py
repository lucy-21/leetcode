"""
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        print(f"{self.val} -> ", end=" ")
        if self.next is not None:
            self.next.print()
        else:
            print(f"end")


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    merged_list = dummy = ListNode()
    while list1 and list2:
        if list1.val <= list2.val:
            merged_list.next = list1
            list1, merged_list = list1.next, merged_list.next
        else:
            merged_list.next = list2
            list2, merged_list = list2.next, merged_list.next

    if list1 or list2:
        merged_list.next = list1 if list1 else list2

    return dummy.next


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    result = mergeTwoLists(list1, list2)
    result.print()
