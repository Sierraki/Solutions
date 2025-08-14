from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction


n = 4
rounds = [1, 3, 1, 2]


def fun(a: int, b: int):
    if a < b:
        for i in range(a + 1, b + 1):
            print(i)
            cnt[i] += 1
    else:
        for i in range(1, b + 1):
            print(i)
            cnt[i] += 1
        for i in range(a+1, n + 1):
            print(i)
            cnt[i] += 1


cnt = Counter([i for i in range(1, n + 1)])

for i in range(1, len(rounds)):
    fun(rounds[i - 1], rounds[i])
cnt[rounds[0]] += 1
tar = max(cnt.values())

ans = [i for i in cnt.keys() if cnt[i] == tar]
print(cnt)
print(ans)


print(fun(3, 1))
