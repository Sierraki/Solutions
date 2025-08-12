from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction


def fun(ans=list, x=int, y=int) -> bool:
    for idx, i in enumerate(ans):
        if x in i and y in i and idx > 1:
            for j in range(1, len(i), 2):
                if (i[j] == x and i[j - 1] == y) or (i[j] == y and i[j - 1] == x):
                    return False
            else:
                return True
    return False


print(fun([[1], [2, None, 3, None, None], [4, None, None]], 4, 5))
print(fun([[1], [2, None, 3, None, None], [4, None, None]], 2, 3))
