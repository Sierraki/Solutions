import bisect
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for idx, i in enumerate(nums):
            if idx == 0:
                nums[idx] = i
            else:
                nums[idx] = i + nums[idx - 1]
        for idx, i in enumerate(queries):
            lc = bisect.bisect(nums, i)
            queries[idx] = lc
        return queries
