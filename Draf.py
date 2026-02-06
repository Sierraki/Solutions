from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate
import heapq

def p(numss):
    for i in numss:
        print(i)


nums = [3, 2, 1, 2, 3, 2, 1]

n = len(nums)


def fun(nums):
    if nums[0]!=nums[1]:
        pf = [1, 2]
    else:
        pf = [1, 1]
    for i in range(2, n):
        if (nums[i - 1] - nums[i - 2]) * (nums[i - 1] - nums[i]) > 0:
            pf.append(pf[-1] + 1)
        else:
            pf.append(2)
    return pf
pf1 = fun(nums)
pf2 = fun(nums[::-1])[::-1]
mx = 0
for i in range(1, n - 1):
    if i == 1:
        if (nums[i + 1] - nums[i - 1]) * (nums[i + 1] - nums[i + 2]) > 0:
            mx = max(mx, pf1[i - 1] + pf2[i + 1])
    elif i < n - 2:
        if (nums[i + 1] - nums[i - 1]) * (nums[i + 1] - nums[i + 2]) > 0:
            mx = max(mx, pf1[i - 1] + pf2[i + 1])
    else:
        if (nums[i - 1] - nums[i - 2]) * (nums[i - 1] - nums[i + 1]) > 0:
            mx = max(mx, pf1[i - 1] + pf2[i + 1])
print(mx)
