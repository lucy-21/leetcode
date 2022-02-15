"""
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
"""

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def reorderLogFiles(logs: List[str]) -> List[str]:
    letter_logs, digit_logs = [], []

    for log in logs:
        if log.split(" ")[1].isnumeric():
            digit_logs.append(log)
        else:
            letter_logs.append(log)

    letter_logs.sort(
        key=lambda log: (log.split(" ")[1:], log.split(" ")[0])
    )  # log.split(" ")[0](identifier) 를 후순위로 정렬
    return letter_logs + digit_logs


if __name__ == "__main__":
    logs = [
        "dig1 8 1 5 1",
        # "let5 art can",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero",
    ]
    result = reorderLogFiles(logs)
    print(result)
