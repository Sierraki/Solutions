import heapq
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

def p(numss):
    for i in numss:
        print(i)



s = "1101"

ans = 0
for i in range(len(s) - 1, 0, -1):
    cur = s[i]
    print(cur)
    if cur == '0':
        ans += 1
    else:
        ans += 2
print(ans)
