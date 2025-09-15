class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mi = min(nums)
        mx = max(nums)
        if mx - mi <= 2 * k:
            return 0
        return mx - mi - 2 * k
