from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction


releaseTimes = [9, 29, 49, 50]
keysPressed = "cbcd"

res = [0] * len(releaseTimes)

res[0] = releaseTimes[0]

for i in range(1, len(res)):
    res[i] = releaseTimes[i] - releaseTimes[i - 1]

cnt = Counter()

for i in range(len(res)):
    cnt[keysPressed[i]] = max(cnt[keysPressed[i]], res[i])

tar = max(cnt.values())

ans = "a"

for i, j in cnt.items():
    if j == tar:
        ans = chr(max(ord(ans), ord(i)))

print(ans)
