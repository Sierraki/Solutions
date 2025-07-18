class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        o_mi = e_mi = float("inf")
        o_mx = e_mx = -float("inf")
        for i in cnt.values():
            if i % 2 == 0:
                e_mi = min(e_mi, i)
                e_mx = max(e_mx, i)
            else:
                o_mi = min(o_mi, i)
                o_mx = max(o_mx, i)
        return max(o_mi - e_mx, o_mx - e_mi)
