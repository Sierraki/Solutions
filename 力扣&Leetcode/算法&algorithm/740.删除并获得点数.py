class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        nums = sorted(list(set(nums)))
        dp = [0] * len(nums)
        for i in range(len(dp)):
            if i == 0:
                dp[0] = cnt[nums[0]] * nums[0]
            elif i == 1:
                if nums[1] - nums[0] == 1:
                    dp[i] = max(dp[i - 1], cnt[nums[i]] * nums[i])
                else:
                    dp[i] = dp[i - 1] + cnt[nums[i]] * nums[i]
            else:
                if nums[i] - nums[i - 1] == 1:
                    dp[i] = max(dp[i - 1], cnt[nums[i]] * nums[i] + dp[i - 2])
                else:
                    dp[i] = dp[i - 1] + cnt[nums[i]] * nums[i]
        return dp[-1]
