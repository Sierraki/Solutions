import heapq
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

def p(numss):
    for i in numss:
        print(i)


ans = 1
cnt = 0
while ans >= 0.5:
    ans = ans * ((1 - 0.005)**cnt)
    cnt += 1
print(cnt, ans)
