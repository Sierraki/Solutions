import heapq
import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
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
    n, m, k = mii()
    nums = lmii()
    ans = 0
    cnt = Counter()
    for i, j in enumerate(nums, 1):
        cnt[i] = j
        if j < k:
            ans += 1
    for _ in range(m):
        a, b = mii()
        if a not in cnt:
            cnt[a] = b
            if b < k:
                ans += 1
        else:
            if cnt[a] < k and b >= k:
                ans -= 1
            elif cnt[a] >= k and b < k:
                ans += 1
            cnt[a] = b
    print(ans)

    pass


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
