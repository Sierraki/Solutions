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
    nums = lmii()
    nums = list(zip(range(n), nums))
    nums = deque(nums)
    res = deque([])
    ans = [-1] * n
    while nums:
        if not res:
            res.appendleft(nums[-1])
            nums.pop()
        else:
            if nums[-1][1] > res[0][1]:
                ans[res[0][0]] = nums[-1][0] + 1
                res.popleft()
            else:
                cur = nums.pop()
                res.appendleft(cur)
    for i in ans:
        print(i)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
