from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

words = ["mass", "as", "hero", "superhero"]
words.sort(key=len, reverse=True)

a = []
b = []
for i in words:
    if i not in a:
        a.append(i)

    for j in a:
        if i in j and i != j:
            b.append(i)
print(b)
