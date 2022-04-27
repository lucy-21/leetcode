"""
Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
"""

import collections, heapq, functools, itertools, re, sys, math, bisect
from typing import *


def licenseKeyFormatting(s: str, k: int) -> str:
    normalized_s = s.replace("-", "")
    share = len(normalized_s) // k
    remain = len(normalized_s) % k

    first_group = normalized_s[:remain]
    remain_groups = normalized_s[remain:]

    result_groups = [remain_groups[i * k : i * k + k] for i in range(0, share)]
    if len(first_group) > 0:
        result_groups = [first_group] + result_groups

    result_str = "-".join(result_groups).upper()
    return result_str


if __name__ == "__main__":
    s = "2-5g-3-J"  # "5F3Z-2e-9-w"
    k = 2  # 4
    result = licenseKeyFormatting(s, k)
    print(result)
