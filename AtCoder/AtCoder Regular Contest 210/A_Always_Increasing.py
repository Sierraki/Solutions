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
    n, q = mii()
    diff = [0] + [1] * (n - 1)
    adds = [0] * (n + 2)
    diff = [0] * (n + 1)
    for _ in range(q):
        i, j = mii()
        adds[i] += j 
        if i < n:
            diff[i] = max(diff[i], adds[i] - adds[i + 1])
    cur = 1 
    total = 1  
    for k in range(1, n): 
        cur += 1 + max(0, diff[k])
        total += cur 
    print(total)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
