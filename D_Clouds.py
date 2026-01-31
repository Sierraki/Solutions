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


def check(cnt):
    ans = 0
    for i in cnt.values():
        ans += len(i)
    return ans


def solve():
    n = ii()
    total = 4000000
    cnt = defaultdict(lambda: Counter())
    nums = [lmii() for _ in range(n)]
    for u, d, l, r in nums:
        for i in range(u, d + 1):
            for j in range(l, r + 1):
                cnt[i][j] += 1
    # 现有的云
    cur_cloud = check(cnt)
    # print(cur_cloud)

    for u, d, l, r in nums:
        cur = cur_cloud
        for i in range(u, d + 1):
            for j in range(l, r + 1):
                if cnt[i][j] - 1 == 0:
                    cur -= 1
        print(total - cur)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
