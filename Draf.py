from collections import defaultdict, Counter
from math import sqrt, floor,gcd
import bisect, re
from collections import deque
from typing import List


s = "010"

cnt = Counter(s)
ans = ""
if cnt["1"] == 1:
    ans += "0" * cnt["0"] + "1"
else:
    ans += "1" * (cnt["1"] - 1) + "0" * cnt["0"] + "1"


print(ans)
