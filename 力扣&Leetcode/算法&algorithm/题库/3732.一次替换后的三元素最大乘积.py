class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        cnt = Counter(nums)
        mi = -(10**5)
        mx = 10**5
        while mx in cnt and cnt[mx] == 1 and len(nums) == 3:
            mx -= 1
        while mi in cnt and cnt[mi] == 1 and len(nums) == 3:
            mi += 1
        a = nums[0] * nums[1] * mi
        b = nums[0] * nums[1] * mx
        c = nums[-1] * nums[-2] * mi
        d = nums[-1] * nums[-2] * mx
        e = nums[-1] * nums[0] * mi
        f = nums[-1] * nums[0] * mx
        return max(a, b, c, d, e, f)
