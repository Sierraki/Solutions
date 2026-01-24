class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) - 1)
        for i in range(len(nums) - 1):
            ans[i] = nums[i] | nums[i + 1]
        return ans
