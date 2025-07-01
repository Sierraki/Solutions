class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        nums = [j for i in obstacleGrid for j in i]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        swap = False
        if nums[-1] == 1:
            return 0
        dp = [0] * m * n
        for i in range(len(dp)):
            if i < n:
                if nums[i] == 0 and not swap:
                    dp[i] = 1
                elif swap:
                    dp[i] = 0
                else:
                    if nums[i] == 1:
                        swap = True
            elif nums[i] == 1:
                dp[i] = 0
            elif i % n == 0 and i > 0:
                dp[i] = dp[i - n]
            else:
                dp[i] = dp[i - 1] + dp[i - n]
        return dp[-1]
