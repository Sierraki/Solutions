from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect, bisect_left
from collections import deque
from typing import List, Optional
from fractions import Fraction


img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]

m = len(img)
n = len(img[0])


ans1 = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        ans = 0
        cnt = 0
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                if 0 <= i + a < m and 0 <= j + b < n:
                    ans += img[i + a][j + b]
                    cnt += 1
        ans1[i][j] = ans // cnt
print(ans1)
