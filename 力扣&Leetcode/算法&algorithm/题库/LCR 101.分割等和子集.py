class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tar = sum(nums) / 2
        if tar != floor(tar):
            return False
        else:
            tar = int(tar)
            dp = [[0] * (tar + 1) for _ in range(len(nums))]
            for i in range(len(nums)):
                for j in range(tar + 1):
                    if i == 0:
                        if nums[i] <= j:
                            dp[0][j] = nums[i]
                    else:
                        if nums[i] <= j:
                            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], nums[i])
                            if j - nums[i] >= 0:
                                cur = j - nums[i]
                                dp[i][j] = max(dp[i][j], nums[i] + dp[i - 1][cur])
                        else:
                            dp[i][j] = dp[i - 1][j]
                    if dp[i][j] == tar:
                        return True
            else:
                return False
