import sys

input = sys.stdin.readline
size = int(input())
for _ in range(size):
    n=int(input())
    if n%2==0:
        print(n//2-1)
    else:
        print(n//2)