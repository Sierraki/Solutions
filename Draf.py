from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction


power = [7, 1, 6, 6]


cnt = Counter(power)

total = sum(power)
ans = 0

for i in list(set(power)):
    a = total
    if i - 1 in cnt:
        a -= cnt[i - 1] * (i - 1)
    print(i, i - 1, a)
    if i - 2 in cnt:
        a -= cnt[i - 2] * (i - 2)
    print(i, i - 2, a)
    if i + 1 in cnt:
        a -= cnt[i + 1] * (i + 1)
    print(i, i + 1, a)
    if i + 2 in cnt:
        a -= cnt[i + 2] * (i + 2)
    print(i, i + 2, a)

    ans = max(a, ans)

print(cnt)

print(ans)
