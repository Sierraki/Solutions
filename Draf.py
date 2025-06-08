from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

x = [1, 2, 1, 3, 2]
y = [5, 3, 4, 6, 2]

a = list(zip(y, x))
a.sort(reverse=True)

l = m = r = 0

while a[l][1] == a[m][1] or a[l][1] == a[r][1] or a[r][1] == a[m][1]:
    if a[l][1] == a[r][1] or a[m][1] == a[r][1]:
        r += 1
    if a[l][1] == a[m][1]:
        m += 1
    if a[l][1] != a[m][1] and a[l][1] != a[r][1] and a[r][1] != a[m][1]:
        break
    if r>len(x)-1:
        print(-1)
res = a[l][0] + a[m][0] + a[r][0]
print(res)
