import bisect
from collections import Counter, defaultdict
from itertools import count
from datetime import datetime

n = 11
a = bin(n)[2:]
for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        print(False)
        break
else:
    print(True)
