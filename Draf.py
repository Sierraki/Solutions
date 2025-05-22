from collections import defaultdict, Counter
from math import sqrt, floor
import bisect

costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
n = len(costs)

for i in range(1, n):
    for j in range(3):
        b = costs[i - 1]
        a = b.copy()
        del a[j]
        costs[i][j] += min(a)

