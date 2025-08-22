class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        pin = 0
        ans = float("inf")
        for idx, i in enumerate(nums):
            if nums[pin] * k < i:
                pin += 1
            ans = min(ans, len(nums) - (idx - pin + 1))
        if ans == float("inf"):
            return 0
        return ans
