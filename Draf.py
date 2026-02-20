from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate
from functools import cache, lru_cache
import heapq
import copy


def p(numss):
    for i in numss:
        print(i)



numBottles = 10
numExchange = 3

a=0.5
b=numExchange-0.5
c=-numBottles

det=b**2-4*a*c

print((-b+ (sqrt(det)))//(2*a))
