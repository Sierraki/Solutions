import heapq
import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

def matt(row, col):
    return [[0] * col for _ in range(row)]

print(matt(2, 3))
