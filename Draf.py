from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache


n = 6
m = 5
k = 5


def min_cut_cost(x, k):
        """计算将长度为 x 的木材切成若干段 (每段 <=k) 的最小成本"""
        if x <= k:
            return 0
        pieces = math.ceil(x / k)
        # 切成 pieces 段的最小成本是：x * (pieces - 1) - k * pieces * (pieces - 1) // 2
        # 也可以用贪心模拟切割过程
        cost = 0
        while x > k:
            # 每次切下一块 k 长度的
            cost += k * (x - k)
            x -= k
        return cost

    # 如果两根木材都不需要切割
    if n <= k and m <= k:
        return 0

    res = float('inf')

    # 枚举第一根切成 a 段，第二根切成 b 段，a + b <= 3
    for a in range(1, 4):  # 第一根最多切 3 段
        for b in range(1, 4 - a + 1):  # 第二根最多切 (3 - a) 段
            if n / a <= k and m / b <= k:
                cost_n = min_cut_cost(n, k)
                cost_m = min_cut_cost(m, k)
                res = min(res, cost_n + cost_m)

    return res