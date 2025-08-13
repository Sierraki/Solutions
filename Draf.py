from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction


s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]


res = dict(zip(indices, s))

ans = ""
for i in range(len(indices)):
    ans += res[i]
print(ans)
