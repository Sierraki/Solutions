from typing import List
import bisect


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect(nums, target)
        return [i for i in range(l, r)]
