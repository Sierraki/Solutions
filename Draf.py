from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache


words = ["hello", "i", "am", "leetcode", "hello"]
aaaaa = [0, 1, 2, 3, 4]
target = "hello"
startIndex = 1
n = len(words)
res = set()
for idx, i in enumerate(words):
    if i == target:
        if idx >= n:
            ans = idx % n
        else:
            ans = idx
        res.add(ans)

print(res)
