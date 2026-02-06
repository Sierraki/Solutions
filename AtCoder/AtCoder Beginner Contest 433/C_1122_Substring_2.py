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
    s = si()
    if len(s) == 1:
        print(0)
    else:
        res = []
        pin = 0
        for i, j in enumerate(s):
            if j == s[pin]:
                continue
            else:
                res.append(s[pin:i])
                pin = i
        if s[pin] != res[-1][-1]:
            res.append(s[pin:])
        cnt = 0
        for i in range(1, len(res)):
            a, b = res[i - 1], res[i]
            if int(a[0]) + 1 == int(b[0]):
                cnt += min(len(a), len(b))
        print(cnt)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
