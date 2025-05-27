class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        def min_cut_cost(x, k):
            if x <= k:
                return 0
            cost = 0
            while x > k:
                cost += k * (x - k)
                x -= k
            return cost

        if n <= k and m <= k:
            print(0)
            return 0
        else:
            res = float("inf")
            for a in range(1, 4):
                for b in range(1, 4 - a + 1):
                    if n / a <= k and m / b <= k:
                        cost_n = min_cut_cost(n, k)
                        cost_m = min_cut_cost(m, k)
                        res = min(res, cost_n + cost_m)
            print(res)
            return res
