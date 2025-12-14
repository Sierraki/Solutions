class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        pf = []
        s = 0
        for i in nums:
            s += i
            pf.append(s)
        dp[k - 1] = pf[k - 1]
        ans = -float("inf")
        for i in range(k, n):
            dp[i] = max(pf[i] - pf[i - k] + dp[i - k], pf[i] - pf[i - k])
            if k == 1:
                dp[i] = max(dp[i], nums[i])
            ans = max(ans, dp[i])
        return max(ans, dp[k - 1])
