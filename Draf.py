from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List

s = "is2 sentence4 This1 a3"

res = s.split()

cnt = {int(i[-1]): i[:-1] for i in res}

print(res)

print(cnt)
