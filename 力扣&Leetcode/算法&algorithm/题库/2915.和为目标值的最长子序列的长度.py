class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0] * (target + 1) for _ in range(n)]
        for i in range(n):
            for j in range(1, target + 1):
                if i == 0:
                    if nums[i] == j:
                        dp[i][j] = 1
                else:
                    if j < nums[i]:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        if j == nums[i]:
                            dp[i][j] = max(1, dp[i - 1][j])
                        # select
                        if j - nums[i] > 0 and dp[i - 1][j - nums[i]] != 0:
                            dp[i][j] = max(dp[i][j], dp[i - 1][j - nums[i]] + 1)
                        # not select
                        dp[i][j] = max(dp[i][j], dp[i - 1][j])
        return dp[-1][-1] if dp[-1][-1] > 0 else -1
