class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter()
        n = len(nums)
        for i in nums:
            cnt[i] += 1
            if cnt[i] > n // 2:
                return i
        return -1
