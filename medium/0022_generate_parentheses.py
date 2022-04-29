"""
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

from audioop import reverse
import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def generateParenthesis(n: int) -> List[str]:
    """
    best solution : https://leetcode.com/problems/generate-parentheses/discuss/10096/4-7-lines-Python
    """

    def gen_parent(prefix: str, counter: int, limit: int, res: List[str]) -> None:
        # print(f"prefix: {prefix}, counter: {counter}, res: {res}")
        if len(prefix) >= 2 * n:
            if counter == 0:
                res.append(prefix)
            return None

        if counter == limit:
            gen_parent(prefix + ")", counter - 1, limit, res)
        elif counter < limit:
            if counter > 0:
                gen_parent(prefix + ")", counter - 1, limit, res)
            gen_parent(prefix + "(", counter + 1, limit, res)

    res = []
    gen_parent("(", 1, n, res)
    return res


if __name__ == "__main__":
    n = 3
    result = generateParenthesis(n)
    print(result)
