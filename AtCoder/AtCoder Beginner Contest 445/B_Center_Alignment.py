from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate as acc
from functools import cache, lru_cache
import heapq
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


def ms(numss):
    return "".join(map(str, numss))


def solve():
    n = ii()
    res = []
    mx = 0
    for _ in range(n):
        cur = si()
        mx = max(mx, len(cur))
        res.append(cur)
    # print(res)
    # print(mx)
    for i in res:
        cur = len(i)
        if cur == mx:
            print(i)
        else:
            left = (mx - cur) // 2
            print("." * left + i + "." * left)

    pass


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
