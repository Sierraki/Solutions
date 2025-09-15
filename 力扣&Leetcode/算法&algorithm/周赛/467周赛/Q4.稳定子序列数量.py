class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        dp = [[0, 0], [0, 0]]
        for num in nums:
            res = num % 2
            tar = 1 - res
            new_c1 = (1 + dp[tar][0] + dp[tar][1]) % mod
            new_c2 = dp[res][0]
            dp[res][0] = (dp[res][0] + new_c1) % mod
            dp[res][1] = (dp[res][1] + new_c2) % mod
        total = (dp[0][0] + dp[0][1] + dp[1][0] + dp[1][1]) % mod
        return total