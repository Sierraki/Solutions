from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

command = "G()(al)"

a = []
n = len(command)
for idx, i in enumerate(command):
    if i == "G":
        a.append(i)
    elif i == "(":
            if command[idx + 1] == "a":
                a.append("al")
            else:
                a.append("o")
print()
