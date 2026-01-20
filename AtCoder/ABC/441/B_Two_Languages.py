import sys

input = sys.stdin.readline
m, n = map(int, input().split())
taka = set(input().split()[0])
aoki = set(input().split()[0])
size = int(input())
res = [input().split()[0] for _ in range(size)]
for i in res:
    t = True
    a = True
    for j in i:
        if j not in taka:
            t = False
        if j not in aoki:
            a = False
    if a == t:
        print("Unknown")
    elif a:
        print("Aoki")
    elif t:
        print("Takahashi")
