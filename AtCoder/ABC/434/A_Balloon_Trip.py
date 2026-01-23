from collections import defaultdict, Counter, deque
from math import sqrt, floor, ceil
from bisect import bisect, bisect_left
from itertools import accumulate
import sys

input = sys.stdin.readline


def mii():
    return map(int, input().split())


def lmii():
    return list(map(int, input().split()))


def ii():
    return int(input())


def si():
    return input()[:-1]


m, n = mii()
print(m * 1000 // n + 1)
