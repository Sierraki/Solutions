from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque


demand = ["acd", "bed", "accd"]

res = set()
for i in demand:
    for j in i:
        res.add(j)
print(len(res))
