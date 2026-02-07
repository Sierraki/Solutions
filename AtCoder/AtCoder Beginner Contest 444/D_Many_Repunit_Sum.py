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
    nums = lmii()

    mx = max(nums)
    cnt = [0] * (mx + 1)

    for i in nums:
        cnt[i] += 1
    cur_idx = 0
    cur = []
    for i in range(mx, 0, -1):
        cur_idx += cnt[i]
        cur.append(cur_idx)
    cur.reverse()
    res = []
    ans = 0
    for val in cur:
        total = val + ans
        res.append(str(total % 10))
        ans = total // 10
    while ans > 0:
        res.append(str(ans % 10))
        ans //= 10
    print("".join(res[::-1]))


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
