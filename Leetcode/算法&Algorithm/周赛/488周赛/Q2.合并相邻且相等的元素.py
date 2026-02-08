class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        nums = deque(nums)
        res = []
        while nums:
            if not res:
                res.append(nums.popleft())
            else:
                if res[-1] == nums[0]:
                    nums[0] *= 2
                    res.pop()
                else:
                    res.append(nums.popleft())
        return res
