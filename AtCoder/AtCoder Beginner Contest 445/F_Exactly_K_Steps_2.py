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
    n, k = mii()

    nums = []
    for _ in range(n):
        nums.append(lmii())

    # print(nums)
    def fun(A, B):
        cur = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                curr = A[i][j]
                if curr == float("inf"):
                    continue
                for k in range(n):
                    new = curr + B[j][k]
                    if new < cur[i][k]:
                        cur[i][k] = new
        return cur

    res1 = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        res1[i][i] = 0
    while k > 0:
        if k & 1:
            res1 = fun(res1, nums)
        nums = fun(nums, nums)
        k >>= 1
    for i in range(n):
        print(res1[i][i])


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
