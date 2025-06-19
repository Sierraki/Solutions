from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque


s = "abaaaaaa"


def fun(s: str):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
        return True


l, r = 0, len(s) - 1
while l < r:
    if s[l] != s[r]:
        print(fun(s[l + 1 : r + 1]) or fun(s[l:r]))
        break
    l += 1
    r -= 1
