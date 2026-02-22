import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from itertools import accumulate as acc
from math import floor, gcd, sqrt

input = sys.stdin.readline


def mii():
    return map(int, input().split())


def lmii():
    return list(map(int, input().split()))


def ii():
    return int(input())


def si():
    return input().strip()


def lacc(nums):
    return list(acc(nums))


def solve():
    n = ii()
    y, r = mii()
    print(min(y // 2 + r, n))


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
