class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        mx = 0
        for i in range(len(nums)):
            if i == 0:
                ans = nums[i]
            else:
                if nums[i - 1] < nums[i]:
                    ans += nums[i]
                else:
                    ans = nums[i]
            mx = max(mx, ans)
        return mx
