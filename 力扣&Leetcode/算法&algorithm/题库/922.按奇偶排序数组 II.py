from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = [i for i in nums if i % 2 == 0]
        even = [i for i in nums if i % 2 != 0]
        for i in range(len(nums)):
            if i % 2 == 1:
                nums[i] = even[-1]
                even.pop()
            else:
                nums[i] = odd[-1]
                odd.pop()
        return nums
