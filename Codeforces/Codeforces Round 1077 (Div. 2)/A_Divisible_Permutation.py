from collections import defaultdict, Counter, deque
from math import sqrt, floor,gcd,ceil
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
    n=ii()
    ans = [0] * n
    left, right = 1, n
    for i in range(n - 1, -1, -1):
        if (n - 1 - i) % 2 == 0:
            ans[i] = left
            left += 1
        else:
            ans[i] = right
            right -= 1
    print(*ans)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
