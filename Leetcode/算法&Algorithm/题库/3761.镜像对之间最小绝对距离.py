class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        ans = float("inf")
        cnt = defaultdict()
        n = len(nums)
        for i, j in enumerate(nums):
            if j in cnt:
                ans = min(ans, i - cnt[j])
            cur = int(str(j)[::-1])
            cnt[cur] = i
        return ans if ans != float("inf") else -1
