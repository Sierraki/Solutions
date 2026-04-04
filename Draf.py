import heapq
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

s1 = "aavizsxpqhxztrwi"
s2 = "zvisqatzpaxhixwr"

def fun(s):
    cnt1 = Counter()
    cnt2 = Counter()
    for i, j in enumerate(s):
        if i % 2 == 0:
            cnt1[j] += 1
        else:
            cnt2[j] += 1
    return [cnt1, cnt2]

nums1 = [1, 3]
nums2 = [3, 1]

print(nums1 == nums2)
