from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


s = "3902"

s = [int(i) for i in str(s)]


def fun(s: list) -> list:
    res = []

    for i in range(1, len(s)):
        res.append((s[i] + s[i - 1]) % 10)

    return res


while len(s) != 2:
    s = fun(s)

print(s)
