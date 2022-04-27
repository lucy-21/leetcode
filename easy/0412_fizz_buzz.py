"""
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""

import collections, heapq, functools, itertools, re, sys, math
from typing import *


def fizzBuzz(n: int) -> List[str]:
    results = []
    for i in range(1, n + 1):
        temp = ""
        if i % 3 == 0:
            temp = temp + "Fizz"
        if i % 5 == 0:
            temp = temp + "Buzz"
        if temp == "":
            temp = str(i)
        results.append(temp)
    return results


if __name__ == "__main__":
    n = 15
    result = fizzBuzz(n)
    print(result)
