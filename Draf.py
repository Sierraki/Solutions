from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

s = "1111011110000011100000110001011011110010111001010111110001"

tar = int(s, 2)
print(tar)
cnt = 0
while tar > 1:
    if tar % 2 == 1:
        tar += 1
    else:
        tar = tar // 2
    cnt += 1
print(cnt)
