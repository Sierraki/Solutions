class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        def fun1(nums, x):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            return left

        def fun2(nums):
            tails = []
            for x in nums:
                idx = fun1(tails, x)

                if idx < len(tails):
                    tails[idx] = x
                else:
                    tails.append(x)
            return len(tails)

        ans = 0
        for i in range(32):
            cur = [j for j in nums if (j >> i) & 1]
            if cur:
                ans = max(ans, fun2(cur))
        return ans
