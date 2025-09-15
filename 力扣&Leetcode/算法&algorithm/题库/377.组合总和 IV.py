class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for j in nums:
                tar = i - j
                if tar >= 0:
                    dp[i] += dp[tar]
        return dp[-1]
