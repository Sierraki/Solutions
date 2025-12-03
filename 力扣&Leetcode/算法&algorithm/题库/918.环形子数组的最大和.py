class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = []
        s = 0
        for i in nums:
            s += i
            res.append(s)
        ans1 = float("inf")
        ans2 = -float("inf")
        mi = mx = res[0]
        for i in range(1, len(res)):
            mi = min(mi, res[i - 1])
            ans2 = max(ans2, res[i] - mi, res[i])
            mx = max(mx, res[i - 1])
            ans1 = min(ans1, res[i] - mx)
        return max(sum(nums) - ans1, ans2)
