from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

grid = [[5, 0, 0, 1], [0, 4, 1, 5], [0, 5, 2, 0], [4, 1, 0, 2]]

nz_cnt=z_cnt=0
n = len(grid)
for i in range(n):
    if grid[i][i] !=0 :
        nz_cnt+=1
for i in range(n - 1, -1, -1):
    if grid[i][i] != 0:
        nz_cnt += 1
for i in grid:
    for j in i:
        if j==0:
            z_cnt+=1
        
