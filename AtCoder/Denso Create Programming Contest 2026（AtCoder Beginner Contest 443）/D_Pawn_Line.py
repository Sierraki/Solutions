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
    nums=lmii()

    # -->
    left = [0] * n
    left[0] = nums[0]
    for i in range(1, n):
        left[i] = min(nums[i], left[i-1] + 1)
    # <--
    right = [0] * n
    right[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        right[i] = min(nums[i], right[i+1] + 1)
    ans = 0
    for i in range(n): 
        res = min(left[i], right[i])
        ans += (nums[i] - res)
    print(ans)

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
