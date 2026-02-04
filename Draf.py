from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate as acc
import heapq
import copy
import sys


numCourses = 2
prerequisites = [[1, 0]]

nums = [[] for _ in range(numCourses)]

for i, j in prerequisites:
    nums[j].append(i)
print(nums)
vis = [0] * numCourses


def dfs(cur):
    if vis[cur] > 0:
        return vis[cur] == 2
    vis[cur] = 1
    for i in nums[cur]:
        if not dfs(i):
            return False
    vis[cur] = 2
    return True

