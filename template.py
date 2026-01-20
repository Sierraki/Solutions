from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
import heapq
import copy
import sys

input = sys.stdin.readline
def mii():
    return map(int, input().split())


def lmii():
    return list(mii())


def ii():
    return int(input())


size = ii()
for _ in range(size):
    n = ii()
    a, b = mii()
    nums = lmii()
