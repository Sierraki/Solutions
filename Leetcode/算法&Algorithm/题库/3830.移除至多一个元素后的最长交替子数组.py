class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        def fun(nums):
            m = len(nums)
            pf = [1] * m
            for i in range(1, m):
                if nums[i] != nums[i - 1]:
                    if (
                        i > 1
                        and (nums[i - 1] - nums[i - 2]) * (nums[i - 1] - nums[i]) > 0
                    ):
                        pf[i] = pf[i - 1] + 1
                    else:
                        pf[i] = 2
                else:
                    pf[i] = 1
            return pf

        pf1 = fun(nums)
        pf2 = fun(nums[::-1])[::-1]
        mx = max(max(pf1), max(pf2)) if n > 0 else 0
        for i in range(1, n - 1):
            if nums[i - 1] == nums[i + 1]:
                continue
            l = pf1[i - 1]
            r = pf2[i + 1]
            if l > 1 and (nums[i - 1] - nums[i - 2]) * (nums[i - 1] - nums[i + 1]) <= 0:
                l = 1
            if r > 1 and (nums[i + 1] - nums[i - 1]) * (nums[i + 1] - nums[i + 2]) <= 0:
                r = 1
            mx = max(mx, l + r)
        return mx
