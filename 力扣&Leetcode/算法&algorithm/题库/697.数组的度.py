class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = defaultdict(list)
        res = []
        tar = max(Counter(nums).values())
        for i, j in Counter(nums).items():
            if j == tar:
                res.append(i)
        for idx, i in enumerate(nums):
            cnt[i].append(idx)
        mx = float("inf")
        for i in res:
            mx = min(mx, (cnt[i][-1] - cnt[i][0] + 1))
        return mx
