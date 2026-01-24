class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        nums = [-i for i in arr[:k]]
        heapq.heapify(nums)
        for i in arr[k:]:
            if -i > nums[0]:
                heapq.heappushpop(nums, -i)
        return [-i for i in nums]
