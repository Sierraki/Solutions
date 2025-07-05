from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque
from typing import List

matrix = [[1, 2], [2, 2]]

m=len(matrix)
n=len(matrix[0])

if m==1:
    print(True)
else:
    for i in range(1,m):
        if n==1:
            print(True)
        else:
            for j in range(1,n):
                if matrix[i][j]!=matrix[i-1][j-1]:
                    print(False)
print(True)
