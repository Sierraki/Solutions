from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque

# 等差求和
# 首项+末项）*项数/2

# x**2+x=2n

n = 5

ans = (-1 + floor(sqrt(1 + 8 * n))) // 2

print(ans)
