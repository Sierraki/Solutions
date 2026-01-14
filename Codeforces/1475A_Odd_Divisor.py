import sys

input = sys.stdin.readline


def fun(n):
    if n % 2 == 1:
        return "YES"
    while n % 2 == 0:
        n = n // 2
    if n > 1:
        return "YES"
    return "NO"


n = int(input())
for _ in range(n):
    num = int(input())
    print(fun(num))
