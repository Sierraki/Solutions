class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def fun(target, nums):
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        for i in range(len(numbers)):
            goal = target - numbers[i]
            lc = fun(goal, numbers)
            if numbers[lc] == goal:
                return [i + 1, lc + 1]
