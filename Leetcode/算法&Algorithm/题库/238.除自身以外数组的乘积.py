from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = [1]
        b = nums.copy()
        n = len(nums)
        for i in range(1, n):
            a.append(a[i - 1] * nums[i - 1])
        res = 1
        for j in range(n - 1, -1, -1):
            if j == n - 1:
                b[j] = res
            else:
                res *= nums[j + 1]
                b[j] = res
        for i in range(n):
            nums[i] = a[i] * b[i]
        return nums
