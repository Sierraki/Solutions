class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        print(nums)
        a = nums[0] * nums[1] * nums[2]
        b = nums[0] * nums[1] * nums[-1]
        c = nums[0] * nums[-1] * nums[-2]
        d = nums[-1] * nums[-2] * nums[-3]
        return max(a, b, c, d)
