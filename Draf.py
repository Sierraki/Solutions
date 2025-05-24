from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re


s = "abcdefg"
shift = [[1, 1], [1, 1], [0, 2], [1, 3]]

n = len(s)
for i in shift:
    a = s + s
    if i[0] == 0:
        a = s + s
        t = i[1] % n
        s = a[t : t + n]
    else:
        t = i[1] % n
        s = a[n - t : 2 * n - t]
    print(s)
print(s)
