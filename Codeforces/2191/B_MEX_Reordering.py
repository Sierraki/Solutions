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


size = ii()
for _ in range(size):
    n = ii()
    nums = lmii()
    nums.sort()
    pf = []
    sf = []
    cur = 0
    for i in nums:
        if i == cur:
            cur += 1
        pf.append(cur)
    cur = 0
    seen = set()
    for i in range(n - 1, -1, -1):
        if nums[i] not in seen:
            seen.add(nums[i])
        while cur in seen:
            cur += 1
        sf.insert(0, cur)
    for i in range(n - 1):
        if pf[i] == sf[i + 1]:
            print("NO")
            break
    else:
        print("YES")
