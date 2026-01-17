import sys

input = sys.stdin.readline
p, q = map(int, input().split())
x, y = map(int, input().split())
if p <= x <= p + 99 and q <= y <= q+ 99 :
    print("Yes")
else:
    print("No")
