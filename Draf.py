from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect, bisect_left
from collections import deque
from typing import List, Optional
from fractions import Fraction


grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]


l = t = float("inf")
r = d = -float("inf")


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]==1:
            l=min(l,j)
            r=max(r,j)
            d=i
            if t== float("inf"):
                t=i


print(l, r, t, d)

ans = (r - l + 1) * (d - t + 1)

print(ans)
