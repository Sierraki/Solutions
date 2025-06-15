class Solution:
    def maxSum(self, nums: List[int]) -> int:
        cnt = defaultdict(list)
        ans = -1
        for i in nums:
            r = max([int(i) for i in str(i)])
            cnt[r].append(i)
        res = [[i, sorted(j, reverse=True)] for i, j in cnt.items() if len(j) >= 2]
        if res:
            for i, j in res:
                ans = max(j[0] + j[1], ans)
        return ans
