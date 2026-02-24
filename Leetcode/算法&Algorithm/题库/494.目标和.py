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
        total = sum(nums)
        po = (total + target) / 2
        n = len(nums)
        if po % 1 == 0 and abs(target)<=total:
            po = int(po)
            dp = [[0] * (po + 1) for _ in range(n)]
            dp[0][0] = 1
            if nums[0] <= po:
                dp[0][nums[0]] += 1
            for i in range(1, n):
                for j in range(po + 1):
                    # 选
                    dp[i][j] = dp[i - 1][j]
                    # 不选
                    if j >= nums[i]:
                        dp[i][j] += dp[i - 1][j - nums[i]]
            return(dp[-1][-1])
        else:
            return 0


