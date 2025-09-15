class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cnt = Counter(nums)
        mx = 1
        for i in cnt:
            if i - 1 not in cnt:
                cur = i
                a = 1
                while cur + 1 in cnt:
                    cur += 1
                    a += 1
                    mx = max(mx, a)
        return mx
