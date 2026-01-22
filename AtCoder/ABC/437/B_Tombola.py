from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
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


h, w, n = mii()
mat = []
for _ in range(h):
    mat.append(lmii())
nums = []
for _ in range(n):
    nums.append(ii())

nums.sort()
ans = cur = 0
for i in range(h):
    cur = 0
    for idx, j in enumerate(mat[i]):
        lc = bisect_left(nums, j)
        if lc < n and lc >= 0:
            if nums[lc] == j:
                cur += 1
                ans = max(ans, cur)
print(ans)
