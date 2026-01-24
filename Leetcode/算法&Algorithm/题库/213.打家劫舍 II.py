class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        nums1 = nums.copy()
        nums2 = nums.copy()
        nums1.pop()
        nums2 = nums2[::-1]
        nums2.pop()
        dp1 = [0] * len(nums1)
        dp1[0] = nums1[0]
        dp1[1] = max(nums1[1], dp1[0])
        for i in range(2, len(dp1)):
            dp1[i] = max(nums1[i] + dp1[i - 2], dp1[i - 1])
        dp2 = [0] * len(nums2)
        dp2[0] = nums2[0]
        dp2[1] = max(nums2[1], dp2[0])
        for i in range(2, len(dp2)):
            dp2[i] = max(nums2[i] + dp2[i - 2], dp2[i - 1])
        return max(dp2[-1], dp1[-1])
