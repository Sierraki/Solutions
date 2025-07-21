from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List

mat = [[2, 2], [25, 23]]
k = 35


def left(arr, k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]


def right(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]


for idx, i in enumerate(mat):
    if idx % 2 == 0:
        mat[idx] = left(i, k)
    else:
        mat[idx] = right(i, k)

print(mat)
