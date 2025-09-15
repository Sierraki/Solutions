class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        mi = float("inf")
        res = []
        for i in cost:
            mi = min(mi, i)
            res.append(mi)
        return res
