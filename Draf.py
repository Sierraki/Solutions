from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


apple = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]


n = sum(apple)
capacity.sort(reverse=True)
s = 0
res = []
for i in capacity:
    s += i
    res.append(s)

print(res)

l, r = 0, len(res) - 1
while l < r:
    m = (l + r) // 2
    if res[m] < n:
        r = m - 1
    else:
        l = m + 1

if res[l] >= n:
    print(l)
