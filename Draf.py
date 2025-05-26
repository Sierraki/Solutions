from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

s1 = "attack"
s2 = "defend"

cnt1 = Counter(s1)
cnt2 = Counter(s2)
if cnt1 != cnt2:
    print(False)
else:
    cnt = defaultdict(int)
    n = len(s1)
    for i in range(n):
        if s1[i] != s2[i]:
            res = tuple(sorted([s1[i], s2[i]]))
            cnt[res] += 1
    if len(cnt) > 1 or max(cnt.values()) > 2:
        print(False)
    else:
        print(True)
