from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque
from typing import List

num = "6777133339"

ans = -float("inf")

for i in range(2, len(num)):
    a = num[i - 2 : i + 1]
    if num[i] == num[i - 1] == num[i - 2]:
        ans = max(ans, int(a))
if ans == -float("inf"):
    print("")
else:
    print(str(ans))
