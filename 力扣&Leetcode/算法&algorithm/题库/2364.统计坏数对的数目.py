class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n - 1) // 2
        cnt = defaultdict(list)
        for i, j in enumerate(nums):
            cnt[j - i].append(j)
        for i in cnt.values():
            if len(i) >= 2:
                total -= len(i) * (len(i) - 1) // 2
        return total
