import sys

input = sys.stdin.readline
size = int(input())
for _ in range(size):
    n = int(input())
    ans = [i for i in range(1, n + 1)]
    print(*ans)
