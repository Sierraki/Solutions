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
    n = ii()
    res = []
    nums = deque(list(range(1, 10)))
    while len(res) < n:
        cur = nums.popleft()
        res.append(cur)
        tar = [-1, 0, 1]
        last = str(cur)[-1]
        for i in tar:
            if 0 <= int(last) + i <= 9:
                ans = str(cur) + str(int(last) + i)
                nums.append(int(ans))
    print(res[-1])


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
