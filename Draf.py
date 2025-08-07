from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod
import bisect, re
from collections import deque
from typing import List

nums = [1, 1, 11, 4, 8, 1]


def fun(n: int) -> bool:

    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
    return True


cnt = Counter(nums)
print(cnt)
for i in cnt.values():
    if fun(i):
        print(True)
print(False)
