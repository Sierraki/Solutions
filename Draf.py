from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate
import heapq
import copy
import sys


def p(numss):
    for i in numss:
        print(i)


nums = [3, 7]

mi = min(nums)
idx = nums.index(mi)

del nums[idx]

if len(nums)>1:
    pf = list(accumulate(nums))
    print(nums)

    print(pf)

    ans = -float("inf")
    l = pf[0]

    for i in range(1, len(pf)):
        if i < len(pf) - 1:
            l = min(l, pf[i - 1])
            ans = max(ans, pf[i] - l, pf[i])
        if i == len(pf) - 1:
            l = min(l, pf[i - 1])
            ans = max(ans, pf[i] - l)

    print(ans)
else:
    print(nums[0])
