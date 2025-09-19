from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect, bisect_left
from collections import deque
from typing import List, Optional
from fractions import Fraction

skills = [4, 18, 17, 20, 15, 12, 8, 5]
k = 1

res = Counter()
for idx, i in enumerate(skills):
    res[i] = idx
skills = deque(skills)
cnt = Counter()
while skills:
    cur = skills.popleft()
    if cur > skills[0]:
        a = skills.popleft()
        skills.append(a)
        cnt[cur] += 1
        if cnt[cur] == k:
            ans = cur
            break
        skills.appendleft(cur)
    else:
        cnt[cur] = 0
        cnt[skills[0]] += 1
        if cnt[skills[0]] == k:
            ans = skills[0]
            break
        skills.append(cur)
print(res[ans])
