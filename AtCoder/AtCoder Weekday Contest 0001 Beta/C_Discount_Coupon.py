import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
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
    nums.sort(reverse=True)
    if k >= len(nums):
        print(0)
    else:
        print(sum(nums[k:]))


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
