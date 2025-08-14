from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction


mat = [[0, 0], [0, 0], [1, 0]]

row = [sum(i) for i in mat]
col = []

for i in range(len(mat[0])):
    a = 0
    for j in range(len(mat)):
        a += mat[j][i]
    col.append(a)


print(row)
print(col)
res = 0
for i in range(len(row)):
    for j in range(len(col)):
        if row[i] == col[j] == 1 and mat[i][j] == 1:
            res += 1
print(res)
