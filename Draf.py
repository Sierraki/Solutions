from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

s = "aababcabc"

cnt = Counter(s[:3])
n = len(s)
c = 0

print(cnt)
for i in range(n):
    if i < 2:
        cnt[s[i]] += 1
    elif i == 2 and len(cnt) == 3:
        c += 1
    elif i > 2:
        cnt[s[i]] += 1
        cnt[s[i - 3]] -= 1
        if cnt[s[i - 3]] == 0:
            del cnt[s[i - 3]]
        if len(cnt) == 3:
            c += 1
        print(cnt, c)
print(c)
