from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect, bisect_left
from collections import deque
from typing import List, Optional
from fractions import Fraction

digits = ""

check = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
ans = deque([])
nums = deque(digits)

while nums:
    cur = nums.popleft()
    if not ans:
        for j in check[cur]:
            ans.append(j)
    else:
        n = len(ans)
        for _ in range(n):
            curr = ans.popleft()
            for j in check[cur]:
                ans.append(curr + j)

print(ans, nums)
