import sys

input = sys.stdin.readline
size = int(input())
for _ in range(size):
    n = int(input())
    if n <= 3:
        print(n)
    else:
        if n % 2 == 0:
            print(0)
        else:
            print(1)
