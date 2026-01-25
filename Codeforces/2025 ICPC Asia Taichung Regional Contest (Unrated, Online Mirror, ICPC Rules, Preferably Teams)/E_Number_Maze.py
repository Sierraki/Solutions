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


def permute(n):
    nums = [int(i) for i in str(n)]
    res = []
    n = len(nums)
    used = [False] * n

    def backtrack(path):
        if len(path) == n:
            res.append(path.copy())
            return
        for i in range(n):
            if used[i] == False:
                path.append(nums[i])
                used[i] = True
                backtrack(path)
                used[i] = False
                path.pop()

    backtrack([])
    res.sort()
    return res


def solve():
    n, j, k = mii()
    res = permute(n)
    a, b = "".join(map(str, res[j - 1])), "".join(map(str, res[k - 1]))
    ans1 = len(a)
    ans2 = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            ans1 -= 1
            ans2 += 1
    print("".join(map(str, [ans2, "A", ans1, "B"])))


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
