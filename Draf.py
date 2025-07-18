from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


s = "aaabaaa"
k = 3


cnt = Counter(s[:k])
if len(cnt) == 1 and s[k] not in cnt:
    print(True)

for i in range(k, len(s)):
    # print(s[i - k], s[i])
    cnt[s[i]] += 1
    cnt[s[i - k]] -= 1
    if cnt[s[i - k]] == 0:
        del cnt[s[i - k]]
    if i < len(s) - 1 and len(cnt) == 1 and s[i + 1] not in cnt and s[i - k] not in cnt:
        print(True)

if len(cnt) == 1 and s[-k - 1] not in cnt:
    print(True)
