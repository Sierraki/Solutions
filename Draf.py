import heapq
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

n = 5

res = bin(n)[2:]
l = n.bit_length()
mask = (1 << l) - 1
print(n ^ mask)
print(mask)
