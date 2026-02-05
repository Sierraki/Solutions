from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate as acc
import heapq
import copy
import sys


def p(numss):
    for i in numss:
        print(i)


accounts = [
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["John", "johnnybravo@mail.com"],
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["Mary", "mary@mail.com"],
]

n = 0
pin = au = len(accounts)

mail_idx = defaultdict()
mail_idx1 = defaultdict()

for i in accounts:
    cur = i[1:]
    for j in cur:
        if j not in mail_idx:
            mail_idx[j] = pin
            mail_idx1[pin] = j
            pin += 1
            n = pin

print(mail_idx)
# print(mail_idx1)

adj = [[] * n for _ in range(au)]

for i in range(au):
    for j in accounts[i][1:]:
        adj[i].append(mail_idx[j])

p(adj)
vis = [False] * n
res = []


def dfs(cur, path):
    path.append(cur)
    vis[cur] = True
    for i in adj[cur]:
        if not vis[i]:
            dfs(i, path)
