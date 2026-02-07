from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate
import heapq
import sys
import copy


def p(numss):
    for i in numss:
        print(i)


n = 4

nums = [[0] * n for _ in range(n)]

dig45 = [True] * (2 * n - 1)
dig135 = [True] * (2 * n - 1)
col = [True] * n

res = []
def check(x, y):
    if col[y] == True:
        if dig45[x + y] == True:
            return dig45[x - y + n] == True
    return False
def tag(x, y):
    col[y] = False
    dig45[x + y] = False
    dig135[x - y + n] = False

def untag(x, y):
    col[y] = True
    dig45[x + y] = True
    dig135[x - y + n] = True

#  当前行
def dfs(cur):
    if cur == n:
        res.append(copy.deepcopy(nums))

    for j in range(n):
        if check(cur, j):
            nums[cur][j] = 1
            tag(cur, j)

            dfs(cur + 1)
            nums[cur][j] = 0
            untag(cur, j)


dfs(0)
p(res)
