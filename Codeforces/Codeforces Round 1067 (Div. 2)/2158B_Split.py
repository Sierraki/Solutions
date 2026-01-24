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
    cnt = Counter(nums)
    ans = oc = ec = 0
    for j in cnt.values():
        if j % 2 == 0:
            ec += 1
        else:
            oc += 1
    if oc > 0:
        print(oc + ec * 2)
    else:
        if ec % 2 == n % 2:
            print(2 * ec)
        else:
            print(2 * (ec - 1))
