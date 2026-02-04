from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate as acc
import heapq
import copy
import sys

input = sys.stdin.readline


def p(nums):
    for i in nums:
        print(i)


def lacc(nums):
    return list(acc(nums))


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

graph = [[1, 2], [2, 3], [5], [0], [5], [], []]


n = len(graph)

adj = [[] for i in range(n)]

for i in range(n):
    for j in graph[i]:
        adj[j].append(i)

print(adj)

tar = [i for i in range(n) if graph[i] == []]

print(tar)

