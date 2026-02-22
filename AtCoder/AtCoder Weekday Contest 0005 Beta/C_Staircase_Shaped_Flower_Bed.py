import heapq
import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

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
    nums = lmii()

    total = sum(nums)
    for i in range(1, n):
        nums[i] = max(nums[i], nums[i - 1] - k)
    for i in range(n - 2, -1, -1):
        nums[i] = max(nums[i], nums[i + 1] - k)
    print(sum(nums) - total)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
