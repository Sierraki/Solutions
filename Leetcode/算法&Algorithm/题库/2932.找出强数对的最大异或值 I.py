class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = -float("inf")
        for i in range(len(nums)):
            for j in range(i + 1):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    ans = max(ans, nums[i] ^ nums[j])
        return ans
