from collections import deque
import sys

input = sys.stdin.readline
size = int(input())
nums = list(map(int, input().split()))
res = []
for x in nums:
    res.append(x)
    if len(res) >= 4:
        if res[-1] == res[-2] == res[-3] == res[-4]:
            for _ in range(4):
                res.pop()
print(len(res))
