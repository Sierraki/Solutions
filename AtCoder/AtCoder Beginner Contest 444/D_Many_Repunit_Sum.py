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
    ans = [0] * (mx + 1)
    nums.sort(reverse=True)
    for i, j in enumerate(nums):
        ans[j] = i + 1
    for i in range(mx - 1, 0, -1):
        ans[i] = max(ans[i], ans[i + 1])
    del ans[0]
    ans += [0]
    for i in range(len(ans)):
        if i < len(ans) - 1:
            if ans[i] >= 10:
                ans[i + 1] += ans[i] // 10
                ans[i] = ans[i] % 10
        else:
            if ans[i] >= 10:
                ans[i] = str(ans[i])[::-1]
    if ans[-1] == 0:
        ans.pop()
    ans = "".join(map(str, ans))[::-1]
    print(ans)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
