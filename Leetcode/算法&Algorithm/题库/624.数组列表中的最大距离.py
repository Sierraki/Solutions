class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mi = []
        mx = []
        for i in arrays:
            mi.append(min(i))
            mx.append(max(i))
        n = len(arrays)
        res1 = min(mi[0], mx[0])
        res2 = max(mi[0], mx[0])
        ans = -float("inf")
        for i in range(1, n):
            res1 = min(res1, mi[i - 1], mx[i - 1])
            res2 = max(res2, mx[i - 1], mi[i - 1])
            ans = max(ans, abs(mx[i] - res1), abs(mi[i] - res2))
        return ans
