import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from math import floor, sqrt

input = sys.stdin.readline


def mii():
    return map(int, input().split())


def lmii():
    return list(map(int, input().split()))


def ii():
    return int(input())


def si():
    return input()[:-1]


a, b = mii()
print(a * 12 + b)
