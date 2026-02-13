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
    n, l, r = mii()
    nums = lmii()
    idx = Counter()
    for i, j in enumerate(nums):
        if j not in idx:
            idx[j] = i
    nums.sort()
    left = bisect_left(nums, l)
    right = bisect(nums, r)
    if left==right:
        print(-1)
    else:
        ans = nums[left:right][-1]
        print(idx[ans] + 1)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
