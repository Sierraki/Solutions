from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
truckSize = 10


nums = sorted(boxTypes, key=lambda x: x[1], reverse=True)
print(nums)

ans = 0
for i in nums:
    if truckSize >= i[0]:
        truckSize -= i[0]
        ans += i[0] * i[1]
        print(truckSize, ans)
    else:
        ans += truckSize * i[1]
        print(truckSize, ans)
        break

print(ans)
