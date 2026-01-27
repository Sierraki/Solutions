from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate as acc
import heapq
import copy


def p(nums):
    for i in nums:
        print(i)


def lacc(nums):
    return list(acc(nums))


n,k=4,1
s='1001'
ans = 0
cnt = 0
for i, j in enumerate(s):
    cnt -= 1
    if j == "1":
        cnt = k
    else:
        if cnt <= 0:
            ans += 1
print(ans)