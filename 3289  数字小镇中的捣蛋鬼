class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        a = []
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                a.append(nums[i])
        return a
