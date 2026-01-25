from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd
from bisect import bisect, bisect_left
from itertools import accumulate as acc
import sys

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
    red = lmii()
    blue = lmii()
    mi = min(-red[0], blue[0])
    mx = max(-red[0], blue[0])
    for i in range(1, n):
        cur = [mi - red[i], mx - red[i], blue[i] - mi, blue[i] - mx]
        mi = mx = cur[0]
        for i in cur:
            mi = min(mi, i)
            mx = max(mx, i)
    print(mx)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
    # solve()
