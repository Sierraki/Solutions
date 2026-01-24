class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total // 2 * 2 != total:
            return False
        else:
            tar = total // 2
            dp = [[0] * (tar + 1) for _ in range(len(nums))]
            for i in range(len(dp)):
                for j in range(1, len(dp[0])):
                    if i == 0:
                        if nums[0] <= j:
                            dp[i][j] = nums[0]
                    else:
                        if nums[i] <= j:
                            dp[i][j] = max(
                                dp[i - 1][j], nums[i], nums[i] + dp[i - 1][j - nums[i]]
                            )
                        else:
                            dp[i][j] = dp[i - 1][j]
                    if dp[i][j] == tar:
                        return True
        return False
