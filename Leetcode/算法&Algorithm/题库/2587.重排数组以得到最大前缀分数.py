class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s <= 0:
                ans = i
                break
            if i == len(nums) - 1 and s > 0:
                ans = i + 1
        return ans
