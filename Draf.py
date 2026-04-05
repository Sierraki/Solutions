import heapq
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]

obstacle_set = set(map(tuple, obstacles)) 
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0   

x, y = 0, 0
mx = 0

for cmd in commands:
    if cmd == -2:  
        d = (d + 3) % 4
    elif cmd == -1:   
        d = (d + 1) % 4
    else:   
        dx, dy = dirs[d]
        for _ in range(cmd): 
            nx, ny = x + dx, y + dy 
            if (nx, ny) in obstacle_set:
                break 
            x, y = nx, ny 
        mx = max(mx, x * x + y * y)

print(mx)
