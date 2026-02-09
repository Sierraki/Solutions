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
    n, m, k = mii()
    cost = []
    gain = []
    for _ in range(n):
        a, b = mii()
        gain.append(a)
        cost.append(b)
    deques = [deque() for _ in range(m + 1)]

    ans = 0

    # 遍历每一个镇子 i
    for i in range(n):
        cur_gain = gain[i]
        cur_cost = cost[i]
        res = []
        if cur_cost <= m:
            res.append((cur_cost, cur_gain))
            ans = max(ans, cur_gain)
        for pre_cost in range(1, m - cur_cost + 1):
            res1 = deques[pre_cost]
            while res1 and res1[0][1] < i - k:
                res1.popleft()

            if res1:
                mx_pre_gain = res1[0][0]

                total_cost = pre_cost + cur_cost
                total_gain = mx_pre_gain + cur_gain

                res.append((total_cost, total_gain))
                ans = max(ans, total_gain)

        for ii, jj in res:
            res1 = deques[ii]

            while res1 and res1[-1][0] <= jj:
                res1.pop()
            res1.append((jj, i))
    print(ans)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
