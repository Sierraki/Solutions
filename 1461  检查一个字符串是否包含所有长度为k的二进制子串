class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)

        nums.sort()
        cur = big = nums[k - 1] - nums[0]


        for i in range(k - 1, n):
            cur = nums[i] - nums[i - k + 1]
            big = min(big, cur)
        return(big)
