class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = []
        s = 0
        for i in nums:
            s += i
            res.append(s)
        mi = 0
        mx = -float("inf")
        dp = [0] * (len(nums))
        dp[0] = res[0]
        for i in range(1, len(nums)):
            mi = min(mi, res[i - 1])
            mx = max(mx, res[i] - mi)
            dp[i] = max(mx, dp[i - 1])
        return dp[-1]
