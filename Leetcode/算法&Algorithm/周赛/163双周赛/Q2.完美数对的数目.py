class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        nums = [abs(x) for x in nums]
        nums.sort()
        ans = 0
        j = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] <= 2 * nums[i]:
                j += 1
            ans += max(0, j - 1 - i)
        return ans