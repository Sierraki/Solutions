from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque
from typing import List


left = 1
right = 22


def check(k: int) -> bool:
    res = []
    for i in str(k):
        if i == "0":
            return False
        res.append(int(i))
    for i in res:
        if k % i != 0:
            return False
    return True


res = []
for i in range(left, right + 1):
    if check(i):
        res.append(i)
print(res)
