from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20],
    [21, 22, 23, 24],
]
result = []
top, bottom = 0, len(matrix) - 1
left, right = 0, len(matrix[0]) - 1

while top <= bottom and left <= right:
    # 从左到右
    for col in range(left, right + 1):
        result.append(matrix[top][col])
    top += 1

    # 从上到下
    for row in range(top, bottom + 1):
        result.append(matrix[row][right])
    right -= 1

    # 从右到左
    if top <= bottom:
        for col in range(right, left - 1, -1):
            result.append(matrix[bottom][col])
        bottom -= 1

    # 从下到上
    if left <= right:
        for row in range(bottom, top - 1, -1):
            result.append(matrix[row][left])
        left += 1

print(result)
