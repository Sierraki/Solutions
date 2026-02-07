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
    nums.sort()

    total = sum(nums)
    res = []

    # print(nums)
    for i in range(1, n + 1):
        if total % i == 0:
            cur = total // i
            # cur为L
            if nums[-1] <= cur:
                l, r = 0, n - 1
                swap = True
                while l <= r:
                    if nums[l] + nums[r] == cur:
                        l += 1
                        r -= 1
                    elif nums[r] == cur:
                        r -= 1
                    else:
                        swap = False
                        break
                if swap == True:
                    res.append(cur)
    res.sort()
    print(*res)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
