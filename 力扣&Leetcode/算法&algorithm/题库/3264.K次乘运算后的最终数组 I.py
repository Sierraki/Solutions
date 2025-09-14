class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        cnt = 0
        while cnt < k:
            minv = 0
            for cur in range(len(nums)):
                if nums[cur] < nums[minv]:
                    minv = cur
            nums[minv] = nums[minv] * multiplier
            cnt += 1
        return nums
