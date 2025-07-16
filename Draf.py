from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


s = "13"
res = []

for i in range(1, len(s)):
    if int(s[i]) % 2 == 0 and int(s[i - 1]) % 2 == 0:
        res.append([i - 1, i])
    elif int(s[i]) % 2 == 1 and int(s[i - 1]) % 2 == 1:
        res.append([i - 1, i])


def fun(s: str, a: int, b: int) -> int:
    s = [i for i in s]
    s[a], s[b] = s[b], s[a]
    return int("".join(s))


ans = res[0]

print(fun(s, ans[0], ans[1]))
