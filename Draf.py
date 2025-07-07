from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque
from typing import List


words = ["pay", "attention", "practice", "attend"]
pref = "at"

ans = 0
for i in words:
    if len(i) >= len(pref):
        if i[: len(pref)] == pref:
            ans += 1
print(ans)
