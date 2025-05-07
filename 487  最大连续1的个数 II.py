from collections import defaultdict
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        left = mx = 0
        for idx, right in enumerate(nums):
            cnt[right] += 1
            while cnt[0] > 1:
                cnt[nums[left]] -= 1
                left += 1
            mx = max(mx, idx - left + 1)
        return mx


eg = Solution()
print(eg.findMaxConsecutiveOnes([1, 0, 1, 1, 0]))  # 4
print(eg.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  # 4
