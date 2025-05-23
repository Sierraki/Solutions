from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re


a = [2, 4, 3]
b = [5, 6, 4]
a = "".join(map(str, a))
b = "".join(map(str, b))
t = str(int(a) + int(b))
print(t)
b = []
for i in range(len(t) - 1, -1, -1):
    b.append(t[i])
print(b)
