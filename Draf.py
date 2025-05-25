from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

s = "abc"


def check(i, j):
    return abs(ord(i) - ord(j)) == 1 or {i, j} == {"a", "z"}


a = []
for i in s:
    if a != [] and check(a[-1], s[0]):
        a.pop()
    else:
        a.append(s[0])
    s = s[1:]
print(a + list(s))
