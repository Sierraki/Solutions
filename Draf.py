from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque


s = "1001"

cnt = Counter(s)
if cnt["1"] > 0 and cnt["0"] == 0 or (cnt["0"] > 0 and cnt["1"] == 0):
    print(True)

for idx, i in enumerate(s):
    if i == "0":
        lc = idx
        break
p = s[lc:]
print(Counter(p)["1"] <= 0)
