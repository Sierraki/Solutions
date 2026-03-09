import heapq
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

ratings = [1, 0, 2]

res = [1] * len(ratings)
for i in range(1, len(ratings)):
    if ratings[i - 1] < ratings[i]:
        res[i] = res[i - 1] + 1
for i in range(len(ratings) - 2, -1, -1):
    if ratings[i  ] > ratings[i+1]:
        res[i]=max(res[i],res[i+1]+1)


print(res)
