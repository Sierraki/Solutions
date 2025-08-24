from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction

n = 10000000

mx = n + 1
primes = []
res = [True] * mx
for i in range(2, mx):
    if res[i]:
        primes.append(i)
        for j in range(i * i, mx, i):
            res[j] = False

print(primes)

ans = []

for i in primes:
    if 1 < i <= n // 2:
        if n - i in primes and n - i > 1:
            ans.append([i, n - i])
print(ans)
