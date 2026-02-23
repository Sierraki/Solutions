import heapq
import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

nums = [2, 6, 4, 8, 10, 9, 15]
nums1 = sorted(nums)

cnt = []

for i in range(len(nums)):
    if nums[i] != nums1[i]:
        cnt.append(i)

print(nums)

print(nums1)


print(cnt)

if cnt:
    print(cnt[-1] - cnt[0] + 1)
else:
    print(0)
