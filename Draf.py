from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

s = "paper"
t = "title"

check={}

for i in range(len(s)):
    if t[i] in check:
        if check[t[i]]!=s[i]:
            print(False)
            break
    else:
        check[t[i]]=s[i]
    if s[i] in check:
        if check[s[i]]!=t[i]:
            print(False)
            break
    else:
        check[s[i]]=t[i]
    