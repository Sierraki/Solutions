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


n = 415

def check(num):
    ans = 1
    for i in range(1, num + 1):
        ans = ans * i
    return ans
ans = 0
for i in str(n):
    ans += check(int(i))
    print(i, check(int(i)))

print(Counter(list(str(n))) == Counter(list(str(ans))))
