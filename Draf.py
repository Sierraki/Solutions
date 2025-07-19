from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


def fib(x: int) -> int:
    if x == 0:
        return 1
    else:
        return 2 * fib(x - 1)


print(fib(10))
print(2**10)
