from collections import defaultdict, Counter
from bisect import bisect
from typing import List
from math import sqrt, floor

mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
col = []
for i in range(len(mat[0])):
    a = []
    for j in mat:
        a.append(j[i])
    col.append(a)
print(mat)
print(col)

rows = [sum(i) for i in mat]
cols = [sum(i) for i in col]
cnt = 0
for i in range(len(rows)):
    if rows[i] + cols[i] == 1:
        cnt += 1
print(rows)
print(cols)
print(cnt)
