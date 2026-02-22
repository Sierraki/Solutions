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


def fun(nums):
    res = [1]
    for i in range(1, len(nums)):
        if res[-1] + 1 <= nums[i]:
            res.append(res[-1] + 1)
        else:
            res.append(min(nums[i], res[-1]))
    return res


def solve():
    n = ii()
    nums = lmii()
    res1 = fun(nums)
    res2 = fun(nums[::-1])[::-1]
    cur = 1
    for i in range(1, n - 1):
        if res2[i + 1] >= res1[i] - 1:
            cur = max(cur, res1[i])
    print(cur)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
