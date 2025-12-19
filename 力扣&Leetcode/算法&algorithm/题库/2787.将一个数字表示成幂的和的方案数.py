class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
        nums = []
        for i in range(1, n + 1):
            if i**x <= n:
                nums.append(i**x)
        dp = [[0] * (n + 1) for _ in range(len(nums))]
        for i in range(1, n + 1):
            cur = nums[0]
            if cur == i:
                dp[0][i] = 1
        for i in range(1, len(nums)):
            cur = nums[i]
            for j in range(1, n + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    if j < cur:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        if j == cur:
                            dp[i][j] += 1
                        # count
                        if j - cur >= 0:
                            dp[i][j] += dp[i - 1][j - cur]
                        # not count
                        dp[i][j] += dp[i - 1][j]
        return dp[-1][-1] % mod
