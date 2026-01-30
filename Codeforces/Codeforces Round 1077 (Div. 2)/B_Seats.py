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


def both(s):
    n = len(s)
    return n//3


def one(s):
    n = len(s)
    return (n+1)//3


def solve():
    # 分区
    n = ii()
    s = si()
    cnt = 0
    for i in s:
        if i == "1":
            cnt += 1
    res = s.split("1")
    if cnt == 0:
        print((n + 2) // 3)
    else:
        m = len(res)
        for i in range(m):
            item = res[i] 
            if len(item) == 0:
                continue 
            if i == 0 or i == m - 1:
                cnt += one(item) 
            else:
                cnt += both(item)
        print(cnt)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
