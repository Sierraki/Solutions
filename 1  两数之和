class Solution:
    def twoSum(self, nums, target):
        a = {}
        for idx, i in enumerate(nums):
            goal = target - i
            if goal not in a:
                a[i] = idx
            else:
                return [a[goal], idx]
