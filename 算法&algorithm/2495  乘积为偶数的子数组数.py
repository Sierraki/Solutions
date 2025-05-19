from typing import List


class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        n = len(nums)
        last_odd = 0
        cnt = 0
        for i in range(n):
            if nums[i] % 2 == 0:
                last_odd = i + 1
            cnt += last_odd
        return cnt


example = Solution()
print(example.evenProduct([9, 6, 7, 13]))  # 6
print(example.evenProduct([7, 3, 5]))  # 0
