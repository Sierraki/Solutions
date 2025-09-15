class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        cnt = Counter()
        mi = 1
        for i in nums:
            if i > 0:
                cnt[i] = 1
            while mi in cnt:
                mi += 1
        return mi
