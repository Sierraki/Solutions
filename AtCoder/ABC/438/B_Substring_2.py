import sys


def fun(a, b):
    a = int(a)
    b = int(b)
    if a >= b:
        return a - b
    return a - b + 10


input = sys.stdin.readline
m, n = map(int, input().split())
a = input()
b = input()
ans = float("inf")
for i in range(m - n + 1):
    cur = 0
    for j in range(n):
        cur += fun(a[i + j], b[j])
    ans = min(ans, cur)
print(ans)
