from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
import logging

# 配置 logging
logging.basicConfig(
    level=logging.DEBUG,  # 设置日志级别
)


a = [1, 2]
n = len(a)

left, right = 0, n - 1
st = True
while left != right and left < n // 2:
    if a[left] == a[right]:
        left += 1
        right -= 1
    else:
        st = False
        break
print(st)
