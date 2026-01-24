import sys

input = sys.stdin.readline
size = int(input())
for _ in range(size):
    n = int(input())
    tar = max(map(int, input().split()))
    print(n * tar)
