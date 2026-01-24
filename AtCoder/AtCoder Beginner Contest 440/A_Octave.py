import sys

input = sys.stdin.readline
a, b = map(int, input().split())
print(a * (2**b))
