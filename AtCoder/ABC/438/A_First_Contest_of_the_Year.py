import sys

input = sys.stdin.readline
a, b = map(int, input().split())
print(7 - (a - b) % (7))
