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


def fun(cur, idx):
    nums[idx] = cur
    ans = idx
    while nums[ans] != 0:
        if ans + cur >= 2 * n:
            break
        ans += cur
    nums[ans] = cur

size = ii()
for _ in range(size):
    n = ii()
    nums = [0] * (2 * n)
    pin = 0
    for i in range(n, 0, -1):
        while nums[pin] != 0:
            pin += 1
        fun(i, pin)
    print(*nums)
