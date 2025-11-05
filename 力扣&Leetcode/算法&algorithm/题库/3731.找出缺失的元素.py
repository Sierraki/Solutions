class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        cnt = Counter([i for i in range(min(nums), max(nums) + 1)])
        for i in nums:
            if i in cnt:
                del cnt[i]
        return sorted([i for i in cnt if cnt[i] == 1])
