import heapq
import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

s = "00110"
k = 2

ans = 2**k

seen = set()

for i in range(len(s) - k + 1):
    seen.add(s[i:i + k])
print(len(seen) == ans)

print(seen, ans)
