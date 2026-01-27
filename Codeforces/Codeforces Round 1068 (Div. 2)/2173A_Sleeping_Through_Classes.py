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
    n, k = mii()
    s = si()
    ans = 0
    cnt = 0
    for i in s:
        cnt -= 1
        if i == "1":
            cnt = k + 1
        else:
            if cnt <= 0:
                ans += 1
    print(ans)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
