from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect
from collections import deque
from typing import List, Optional
from fractions import Fraction
import pandas as pd


import math

nums = [2, 5, 3, 1, 4]


def fun1(nums):
    n = len(nums)
    K = int(math.log2(n)) + 1
    st = [[0] * K for _ in range(n)]
    for i in range(n):
        st[i][0] = nums[i]
    j = 1
    while (1 << j) <= n:
        i = 0
        while i + (1 << j) <= n:
            st[i][j] = max(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
            i += 1
        j += 1
    return st


def fun2(st, L, R):
    if L > R:
        return -(10**18)
    j = int(math.log2(R - L + 1))
    return max(st[L][j], st[R - (1 << j) + 1][j])


n = len(nums)
if n < 3:
    print(0)
st = fun1(nums)
cnt = 0
for l in range(n - 2):
    for r in range(l + 2, n):
        mx = fun2(st, l + 1, r - 1)
        if nums[l] > mx and nums[r] > mx:
            cnt += 1
print(cnt)


# print(count_bowl_subarrays([2, 5, 3, 1, 4]))  # 2
# print(count_bowl_subarrays([5, 1, 2, 3, 4]))  # 3
# print(count_bowl_subarrays([1000000000, 999999999, 999999998]))  # 0
