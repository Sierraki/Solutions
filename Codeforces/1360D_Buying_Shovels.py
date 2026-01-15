from math import floor, sqrt
import sys

input = sys.stdin.readline
size = int(input())
for _ in range(size):
    a, b = map(int, input().split())
    mx = a
    for i in range(1, floor(sqrt(a)) + 1):
        if a % i == 0:
            if i <= b:
                mx = min(mx, a // i)
            if a // i <= b:
                mx = min(mx, i)
    print(mx)
