class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        lmi = [0] * n
        rmi = [0] * n
        ans = nums[0]
        for i in range(n - 1):
            ans = min(ans, nums[i])
            lmi[i] = min(ans, nums[i])
        ans = nums[-1]
        for i in range(n - 1, 0, -1):
            ans = min(ans, nums[i])
            rmi[i] = min(ans, nums[i])
        res = float("inf")
        for i in range(1, n - 1):
            if nums[i] > lmi[i - 1] and nums[i] > rmi[i + 1]:
                res = min(res, nums[i] + lmi[i - 1] + rmi[i + 1])
        if res == float("inf"):
            return -1
        return res
