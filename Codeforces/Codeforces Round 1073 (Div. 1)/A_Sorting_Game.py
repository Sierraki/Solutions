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
    nums = list(map(int, si()))
    if sorted(nums) == nums:
        print("Bob")
    else:
        print("Alice")
        tar = sorted(nums)
        res = []
        for i in range(n):
            if nums[i] != tar[i]:
                res.append(i + 1)
        print(len(res))
        print(*res)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
