from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate as acc
import heapq
import copy
import sys


weight = [2, 5, 1, 4, 3]

nums = deque(weight)

cnt = 0
res = []
while nums:
    if not res:
        res.append(nums.popleft())

    cur=   nums.popleft() 
    if res[-1] > cur:
        res.pop()
        cnt += 1
    else:
        res.append(cur)
    print(res, nums)

print(cnt)
