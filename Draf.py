from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate as acc
import sys

n = 5
relation = [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]]
k = 3


adj = [[] for _ in range(n)]

# print(adj)

for i, j in relation:
    adj[i].append(j)

print(adj)


nums = deque([0])

for _ in range(k):
    size = len(nums)
    for _ in range(size):
        cur = nums.popleft()
        for i in adj[cur]:
            nums.append(i)

cnt = 0
for i in nums:
    if i == n - 1:
        cnt += 1
print(cnt)
