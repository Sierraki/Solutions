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


def ms(numss):
    return "".join(map(str, numss))


def solve():
    n = ii()
    nums = lmii()

    limi = 450
    ans = 0
    for i in range(1, limi + 1):
        for j in range(n):
            if j - nums[j] * i >= 0:
                if nums[j - nums[j] * i] == i:
                    ans += 1
    for i in range(n):
        if nums[i] > limi:
            for k in range(1, (n - 1 - i) // nums[i] + 1):
                if nums[i + nums[i] * k] == k:
                    ans += 1

    print(ans)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
