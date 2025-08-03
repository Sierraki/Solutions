from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List

s = "10#11#12"


pin = len(s) - 1
cnt = {i - 96: chr(i) for i in range(ord("a"), ord("z") + 1)}
res = ""

while pin >= 0:
    if s[pin].isdigit():
        res += cnt[int(s[pin])]
        pin -= 1
    elif s[pin] == "#":
        res += cnt[int(s[pin - 2 : pin])]
        pin -= 3


# ans = "".join(res)
print(res[::-1])
# print(ans)
