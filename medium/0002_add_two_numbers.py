"""
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""

from audioop import reverse
import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(self):
        print(f"{self.val} -> ", end=" ")
        if self.next is not None:
            self.next.print()
        else:
            print(f"end")


def gen_list_node(list: List[int]) -> ListNode:
    node = None
    if list:
        node = ListNode(list[0])
        node.next = gen_list_node(list[1:])
    return node


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l1_vals = []
    l2_vals = []

    while l1:
        l1_vals = [l1.val] + l1_vals
        l1 = l1.next
    while l2:
        l2_vals = [l2.val] + l2_vals
        l2 = l2.next

    l1_val = int("".join([str(val) for val in l1_vals]))
    l2_val = int("".join([str(val) for val in l2_vals]))
    sum = l1_val + l2_val
    sum_vals = list(reversed([int(val) for val in str(sum)]))

    return gen_list_node(sum_vals)


if __name__ == "__main__":
    l1 = gen_list_node([2, 4, 3])
    l2 = gen_list_node([5, 6, 4])
    l1.print()
    l2.print()

    result = addTwoNumbers(l1, l2)
    result.print()
