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
    nums = lmii()
    cnt = Counter()
    for i, j in enumerate(nums):
        cnt[j] = i
    lc = -1
    tar = -1
    for i, j in enumerate(nums):
        if j != n - i:
            lc = i
            tar = cnt[n - i]
            break
    if lc == -1:
        res = nums
    else:
        if lc < tar:
            p1 = nums[:lc]
            p2 = nums[lc : tar + 1]
            p3 = nums[tar + 1 :]
            res = p1 + p2[::-1] + p3
        else:
            p1 = nums[:tar]
            p2 = nums[tar : lc + 1]
            p3 = nums[lc + 1 :]
            res = p1 + p2[::-1] + p3
    print(*res)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
