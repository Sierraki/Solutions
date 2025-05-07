import bisect
from sortedcontainers import SortedList
from collections import defaultdict, Counter

nums = [1, 0, 1, 1, 0]

cnt = defaultdict(int)

left = mx = 0

for idx, right in enumerate(nums):
    cnt[right] += 1
    while cnt[0] > 1:
        cnt[nums[left]] -= 1
        left += 1
    mx = max(mx, idx - left + 1)
    print(mx)
