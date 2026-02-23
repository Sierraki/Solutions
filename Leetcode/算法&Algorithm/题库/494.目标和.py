# 递归做法
from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(index, current_sum):
            if index == n:
                return 1 if current_sum == target else 0
            add_ways = dfs(index + 1, current_sum + nums[index])
            sub_ways = dfs(index + 1, current_sum - nums[index])
            return add_ways + sub_ways

        return dfs(0, 0)
# 动态规划
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        if total < abs(target) or (total + target) % 2 != 0:
            return 0
        po = (total + target) // 2
        dp = [[0] * (po + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            num = nums[i - 1]
            for j in range(po + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]
        return dp[-1][-1]
