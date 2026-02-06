from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate
import heapq
import sys

def p(numss):
    for i in numss:
        print(i)


s = ")()())"

res = []
ans = 0

for i, j in enumerate(s):
    if j == "(":
        res.append(i)
    else:
        if res:
            cur = res.pop()

            ans = max(ans, i - cur - 1)

        else:
            res.append(i)
    print(res, ans)

print(ans)
