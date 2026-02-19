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

s = "00110011"

# n=len(s)

res = []

pin = 0

for i, j in enumerate(s):
    if j == s[pin]:
        continue
    else:
        res.append(i - pin)
        pin = i
if pin!=len(s):
    res.append(len(s)-pin)
cnt = 0
for i in range(1, len(res)):
    cnt += min((res[i]), (res[i - 1]))
print(res)
print(cnt)
