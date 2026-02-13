from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate
from functools import cache
import heapq
import sys
import copy


def p(numss):
    for i in numss:
        print(i)

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]


@cache
def dfs(cur):
    if cur <= 1:
        return 0

    return min(dfs(cur - 1) + cost[cur - 1], dfs(cur - 2) + cost[cur - 2])


print(dfs(len(cost)))
