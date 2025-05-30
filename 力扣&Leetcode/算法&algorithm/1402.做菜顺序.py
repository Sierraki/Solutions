class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        a = []
        s = 0
        for i in satisfaction:
            s += i
            a.append(s)
        mx = cur = 0
        for i in a:
            cur += i
            mx = max(cur, mx)
        return mx
