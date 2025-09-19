from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect, bisect_left
from collections import deque
from typing import List, Optional
from fractions import Fraction

word = "aaaaaaaaaaaaaabb"

ans = ""
res = deque([])
word = deque(word)

while word:
    if (not res or word[0] == res[-1]) and len(res) < 9:
        cur = word.popleft()
        res.append(cur)

    elif word[0] != res[-1] or len(res) == 9:
        n = len(res)
        ans += f"{n}{res[-1]}"
        res.clear()
    print(ans, res, word)

n = len(res)
ans += f"{n}{res[-1]}"

print(ans, res, word)
