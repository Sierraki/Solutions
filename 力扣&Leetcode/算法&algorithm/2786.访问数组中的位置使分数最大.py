class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        even = odd = -float("inf")
        for i in range(len(nums)):
            if i == 0:
                if nums[i] % 2 == 0:
                    even = nums[i]
                else:
                    odd = nums[i]
            else:
                if nums[i] % 2 == 0:
                    even = max(even + nums[i], odd + nums[i] - x)
                else:
                    odd = max(odd + nums[i], even + nums[i] - x)
        return max(odd, even)
