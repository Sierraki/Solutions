from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


n = 26

ans1 = n // 7
ans2 = n % 7

print(ans1, ans2)

res = 0

if ans1 > 0:
    res += ans1 * 28 + (ans1) * (ans1 - 1) // 2 * 7
    print(res)

if ans2 > 0:
    s = 0
    for i in range(1, ans2 + 1):
        s += i + ans1
    print(s)
    res += s

print(res)
