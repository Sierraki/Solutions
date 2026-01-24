from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate
import sys

input = sys.stdin.readline


def mii():
    return map(int, input().split())


def lmii():
    return list(map(int, input().split()))


def ii():
    return int(input())


def si():
    return input()[:-1]


n, m = mii()
nums1 = lmii()
nums2 = lmii()
ans = 0
nums2.sort()
pf = list(accumulate(nums2, initial=0))
for i in nums1:
    tar = bisect(nums2, i)
    ans -= pf[tar]
    ans += pf[-1] - pf[tar]
    ans += tar * i
    ans -= (m - tar) * i
print(abs(ans) % 998244353)
