class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return -1
        nums.sort()
        # binary search
        ans = -1
        for idx, i in enumerate(nums):
            tar = k - i
            if tar < 0:
                break
            numm = nums.copy()
            del numm[idx]
            lc = bisect.bisect_left(numm, tar)
            if numm[lc - 1] + i < k:
                ans = max(ans, numm[lc - 1] + i)
        return ans
