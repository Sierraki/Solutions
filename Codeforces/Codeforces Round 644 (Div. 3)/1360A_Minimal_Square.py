import sys

input = sys.stdin.readline
size = int(input())
for _ in range(size):
    a, b = map(int, input().split())
    print(min(max(a * 2, b), max(a, b * 2)) ** 2)
