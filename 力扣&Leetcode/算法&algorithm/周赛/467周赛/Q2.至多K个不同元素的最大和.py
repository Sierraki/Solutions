class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = list(set(nums))
        nums.sort(reverse=True)
        ans = k
        for i in range(k + 1):
            if i < len(nums) and nums[i] < 0:
                ans = i
                break
        return nums[:ans]