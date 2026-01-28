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
    H, W, N, h, w = mii()
    nums = [lmii() for _ in range(H)]
    cnt = Counter(j for i in nums for j in i)
    for i in range(H - h + 1):
        cur = cnt.copy()
        ans = []
        for j in range(W - w + 1):
            if j == 0:
                for ii in range(i, i + h):
                    for jj in range(j, j + w):
                        cur[nums[ii][jj]] -= 1
                        if cur[nums[ii][jj]] == 0:
                            del cur[nums[ii][jj]]
                ans.append(len(cur))
            else:
                # 宽度
                # print(j - 1, j + w - 1)
                # 高度
                # print(i,i+h)
                for k in range(i, i + h):
                    cur[nums[k][j + w - 1]] -= 1
                    cur[nums[k][j - 1]] += 1
                    if cur[nums[k][j + w - 1]] == 0:
                        del cur[nums[k][j + w - 1]]
                ans.append(len(cur))
        print(*ans)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
