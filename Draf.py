from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

nums = [-3, 2, -3, 4, 2]

s = 0
mi = float("inf")
for i in nums:
    s += i
    mi = min(s, mi)
print(mi)
