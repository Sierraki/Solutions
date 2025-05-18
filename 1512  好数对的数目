class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    cnt += 1
        return cnt
