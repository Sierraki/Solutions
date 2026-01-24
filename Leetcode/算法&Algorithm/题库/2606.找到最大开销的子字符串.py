class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        cnt = dict(zip(chars, vals))
        res = []
        su = 0
        for i in s:
            if i in cnt:
                su += cnt[i]
            else:
                su += ord(i) - 96
            res.append(su)
        ans = max(0, res[0])
        mi = float("inf")
        for i in range(1, len(res)):
            mi = min(mi, res[i - 1])
            ans = max(ans, res[i] - mi, res[i])
        return ans
