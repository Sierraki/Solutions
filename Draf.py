from typing import List
from math import sqrt, floor

m = 2
n = 3
indices = [[0, 1], [1, 1]]
row = [0] * n
print(row)
ma = []
for _ in range(m):
    ma.append(row)
print(ma)
for i in indices:
    # row
    for j in range(n):
        ma[i[0]][j] += 1
    # col
    for k in range(m):
        ma[k][i[1]] += 1
    print(ma)
