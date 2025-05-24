from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re


a = [2, 4, 3]
b = [5, 6, 4]

for i in a:
    b.insert(0,i)
print(b)