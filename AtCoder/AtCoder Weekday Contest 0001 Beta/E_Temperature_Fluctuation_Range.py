import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

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
    n, k = mii()
    nums = lmii()
    cur_mi = deque([])
    cur_mx = deque([])
    ans = 0
    for i, j in enumerate(nums):
        if cur_mi and cur_mi[0] <= i - k:
            cur_mi.popleft()
        while cur_mi and nums[cur_mi[-1]] >= j:
            cur_mi.pop()
        cur_mi.append(i)
        if cur_mx and cur_mx[0] <= i - k:
            cur_mx.popleft()
        while cur_mx and nums[cur_mx[-1]] <= j:
            cur_mx.pop()
        cur_mx.append(i)
        if i >= k - 1:
            ans = max(ans, abs(nums[cur_mx[0]] - nums[cur_mi[0]]))
    print(ans)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
