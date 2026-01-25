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


def fun(nums, tar):
    left, right = 0, len(nums) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= tar:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans


def solve():
    n = ii()
    sow = lmii()
    lv = lmii()
    cnt = Counter()
    sow.sort(reverse=True)
    for i, j in enumerate(sow):
        cnt[j] = i + 1
    pf = lacc(lv)
    ans = 0
    for i, j in cnt.items():
        cur = fun(pf, j)
        if cur != -1:
            ans = max(ans, (cur + 1) * i)
    print(ans)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
