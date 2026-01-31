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


def solve():
    n, t = mii()
    nums = lmii()
    shut = [[t, False]]
    op = [[0, True]]
    for i in nums:
        shut.append([i, False])
        if op[-1][0] < i:
            op.append([i + 100, True])
    res = op + shut
    res.sort()
    cnt = 0
    for i in range(1, len(res)):
        cur = res[i]
        pre = res[i - 1]
        if cur[0] <= t:
            if pre[1] == True:
                cnt += cur[0] - pre[0]
    print(cnt)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
