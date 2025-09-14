class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        while l < r:
            if nums[l] + nums[r] <= target:
                ans += r - l
                l += 1
            else:
                r -= 1
        return ans % (10**9 + 7)
