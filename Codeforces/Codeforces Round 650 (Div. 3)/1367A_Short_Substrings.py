import sys

input = sys.stdin.readline
size = int(input())
for _ in range(size):
    s = input()
    res = s[0]
    for i in range(1, len(s), 2):
        res += s[i]
    print(res)
