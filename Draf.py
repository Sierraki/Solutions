from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
import logging

# 配置 logging
logging.basicConfig(
    level=logging.DEBUG,  # 设置日志级别
)


nums = [1, 2, 8]
target = 4

sum = 1
for i, x in enumerate(nums):
    if (target % x):
        return False
    sum *= x
    
if sum / target == target:
    return True
    
return False      