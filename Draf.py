from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

arr = [-10, 12, -20, -8, 15]

st = False
a = set()
for i in arr:
    if i % 2 == 0:
        a.add(i // 2)
    if i in a:
        st = True
print(st)
