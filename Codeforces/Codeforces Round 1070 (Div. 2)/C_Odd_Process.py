from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate
import sys

input = sys.stdin.readline


def mii():
    return map(int, input().split())


def lmii():
    return list(map(int, input().split()))


def ii():
    return int(input())


def si():
    return input()[:-1]


size = ii()
for _ in range(size):
    n = ii()
    nums = lmii()
    even = []
    odd = []
    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    even.sort(reverse=True)
    pf = list(accumulate(even))
    pf = [0] + pf
    odd.sort()
    res = []
    if even and odd:
        for i in range(1, n + 1):
            if i <= len(even) + 1:
                cur = odd[-1] + pf[i - 1]
            elif len(even) + 1 < i < n:
                if (i - len(even)) % 2 == 0:
                    cur = odd[-1] + pf[-2]
                else:
                    cur = odd[-1] + pf[-1]
            else:
                if len(odd) % 2 == 0:
                    cur = 0
                else:
                    cur = odd[-1] + pf[-1]
            res.append(cur)
    elif even:
        res = [0] * n
    else:
        res = [odd[-1] if i % 2 == 0 else 0 for i in range(n)]
    print(*res)
