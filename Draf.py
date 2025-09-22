from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect, bisect_left
from collections import deque
from typing import List, Optional
from fractions import Fraction


nums = [1, 2, 1, 1, 2, 1, 2]


cnt = Counter()

odd = True
odd_len = 0

even = True
even_len = 0

for i in nums:
    if i%2== 1:
        if odd == True:
            odd_len += 1
            odd = False
        if even == False:
            even_len += 1
            even = True
        cnt[1]+=1
    else:
        if odd == False:
            odd_len += 1
            odd = True
        if even == True:
            even_len += 1
            even = False
        cnt[0]+=1
print(odd_len)
print(even_len)

print(nums)
print(cnt)

ans = max(cnt[1], cnt[0], odd_len, even_len)
print(ans)
