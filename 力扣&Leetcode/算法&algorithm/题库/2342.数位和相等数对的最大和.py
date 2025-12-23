class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        cnt = defaultdict(list)
        for i in nums:
            res = 0
            for j in str(i):
                res += int(j)
            cnt[res].append(i)
        ans = -1
        for i, j in cnt.items():
            if len(j) >= 2:
                j.sort(reverse=True)
                ans = max(ans, sum(j[:2]))
        return ans
