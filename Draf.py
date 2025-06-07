from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

arr = [18, 12, -18, 18, -19, -1, 10, 10]

tar = sum(arr) / 3
print(sum(arr), tar)
left, right = 0, len(arr) - 1
sl, sr = 0, 0
lc1, lc2 = -1, -1

while left < len(arr):
    sl += arr[left]
    if sl == tar:
        lc1 = left
        break
    left += 1
print(lc1)


while right > 0:
    sr += arr[right]
    if sr == tar:
        lc2 = right
        break
    right -= 1

a = sum(arr[: lc1 + 1])
b = sum(arr[lc2:])
c = sum(arr) - b - a

print(a, b, c, a == b == c)
