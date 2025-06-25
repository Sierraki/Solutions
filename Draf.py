from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque


date = "2003-12-27"

y = int(date[:4])
m = int(date[5:7])
d = int(date[8:])
print(y, m, d)
# 判断闰年还是平年
if y % 4 == 0 and y % 100 != 0 or (y % 400 == 0):
    A = True
else:
    A = False
# 闰年
a = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
# 平年
b = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

if A == True:
    ans = a[m - 1] + d
else:
    ans = b[m - 1] + d
print(ans)
