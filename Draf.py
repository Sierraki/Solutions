from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

satisfaction = [5, 0, -1, -8, -9]
satisfaction.sort(reverse=True)
a = []
s = 0
for i in satisfaction:
    s += i
    a.append(s)
print(satisfaction)
print(a)
mx = cur = 0
for i in a:
    cur += i
    mx = max(cur, mx)
print(mx)
