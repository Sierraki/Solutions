class Solution(object):
    def pivotIndex(self, nums):
        l = 0
        r = sum(nums)
        ans = -1
        for idx, i in enumerate(nums):
            if idx > 0:
                l += nums[idx - 1]
            r -= i
            if l == r:
                return idx
        return ans
