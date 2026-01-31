class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        mx = 1
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    mx = max(dp[i], mx)
        return mx


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if not res:
                res.append(i)
            else:
                if i > res[-1]:
                    res.append(i)
                else:
                    # 大于某数的最小数
                    lc = bisect_left(res, i)
                    res[lc] = i
        return len(res)
