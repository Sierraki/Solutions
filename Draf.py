from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List

word1 = "aaaa"
word2 = "bccb"

cnt1 = Counter(word1)
cnt2 = Counter(word2)
cnt = set(word1 + word2)

for i in cnt:
    print(i)
