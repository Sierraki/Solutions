class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = []
        for i in nums:
            if cnt[i] <= 1:
                res.append(i)
        if not res:
            return -1
        return max(res)
