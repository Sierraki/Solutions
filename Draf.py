from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate
import heapq
import copy


def p(numss):
    for i in numss:
        print(i)


nums = [7, 2, 4]
k = 2

cur = deque([])
ans = []

for i, j in enumerate(nums):
    if cur and cur[0]<=i-k:
        cur.popleft()
    while cur and nums[cur[-1]]<=j:
        cur.pop()
    cur.append(i)
    if i>=k-1:
        ans.append(nums[cur[0]])
print(ans)
