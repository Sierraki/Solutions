from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
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


def lap(range1, range2):
    a, b = range1
    x, y = range2
    start = max(a, x)
    end = min(b, y)
    if start <= end:
        return [start, end]
    else:
        return [-1, -1]


def solve():
    n, h = mii()
    t = [0] * (n + 1)
    mi = [0] * (n + 1)
    mx = [0] * (n + 1)
    mi[0] = mx[0] = h
    swap = False
    for times in range(n):
        i, j, k = mii()
        tar = [j, k]
        dif = i - t[times]
        t[times + 1] = i
        cur = [mi[times] - dif if mi[times] - dif > 0 else 1, mx[times] + dif]
        res = lap(cur, tar)
        if res == [-1, -1]:
            if not swap:
                print("No")
                swap = True
        else:
            mi[times + 1], mx[times + 1] = res[0], res[1]
    if not swap:
        print("Yes")


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
