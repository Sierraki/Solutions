from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect, bisect_left
from collections import deque
from typing import List, Optional
from fractions import Fraction


hours = [13, 11]


cnt = Counter()
for i in hours:
    if i % 24 == 0:
        cnt[0] += 1
    else:
        cnt[i % 24] += 1
print(cnt)
ans = 0
check = Counter()
for i, j in cnt.items():
    if i == 0:
        ans += (j - 1) * j // 2
    else:
        tar = 24 - i
        if tar == i:
            ans += (j - 1) * j // 2
        else:
            if tar in cnt and tar not in check:
                ans += j * cnt[tar]
                check[tar] += 1
                check[i] += 1
print(ans)
