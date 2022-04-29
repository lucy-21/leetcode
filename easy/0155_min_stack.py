"""
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


class MinStack:
    """
    stack 안에 (val, 해당 val이 들어온 시점까지 최소값) 저장
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        current_min = self.getMin()
        if current_min == None or val < current_min:
            current_min = val
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][1]


if __name__ == "__main__":
    minStack = MinStack()
    print(minStack.push(-2))
    print(minStack.push(0))
    print(minStack.push(-3))
    print(minStack.getMin())  # return -3
    print(minStack.pop())
    print(minStack.top())  # return 0
    print(minStack.getMin())  # return -2
