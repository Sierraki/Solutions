class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs = sorted(costs, key=lambda x: x[0] - x[1])
        p1 = sum([i for i, j in costs[:n]])
        p2 = sum([j for i, j in costs[n:]])
        return p1 + p2
