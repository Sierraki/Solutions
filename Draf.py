from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


s = "LLLLRRRR"

cnt = Counter()

ans=0
l = r = 0
while l <= r and r < len(s):
    cnt[s[r]] += 1
    if cnt["L"] == cnt["R"]:
        ans+=1
        r += 1
        l = r
    else:
        r += 1

print(ans)
