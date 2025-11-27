class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] + [float("inf")] * (n)
        costs.insert(0, 0)
        for i in range(n + 1):
            for j in range(1, 4):
                if 0 <= i - j <= n:
                    dp[i] = min(dp[i], dp[i - j] + costs[i] + j**2)
        return dp[-1]
