class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return max(cnt, key=lambda x: cnt[x])
