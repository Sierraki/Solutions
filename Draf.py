from collections import defaultdict, Counter
from sortedcontainers import SortedList
from math import sqrt, floor, gcd, lcm, prod, ceil
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction

words = ["aaa", "c", "aba"]
words.sort()
res = []

for i in words:
    a = deque([j for j in i])
    cnt = 0
    while a:
        cur = a.popleft()
        if not res:
            res.append(cur)
        if res[-1] == cur and cnt < 1:
            cnt += 1
            continue
        else:
            res.append(cur)
print(res)
