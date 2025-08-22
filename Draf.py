from collections import defaultdict, Counter
from sortedcontainers import SortedList
from math import sqrt, floor, gcd, lcm, prod, ceil
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction

words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

cnt = dict(zip(order, [str(i) for i in range(1, 27)]))


m = len(words)
n = 0
for i in words:
    n = max(n, len(i))

res = [["00"] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if j < len(words[i]):
            res[i][j] = cnt[words[i][j]].zfill(2)
for idx, i in enumerate(res):
    res[idx] = int("".join(i))

print(res)
