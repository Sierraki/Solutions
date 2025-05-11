from typing import List


class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
        nums = [i for i in range(target)]
        left, right = 0, 1
        cur = nums[left]
        a = []
        while right < target:
            if cur < target:
                cur += nums[right]
                right += 1
            if cur >= target:
                cur -= nums[left]
                left += 1
            if cur == target:
                a.append(nums[left:right])
        a.sort()
        return a
