class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums)):
            nums[i] = sum(map(int, str(nums[i])))
            if nums[i] == i:
                ans = i
                break
        return ans
