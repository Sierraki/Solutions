class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        res = cost[::-1]
        ans = 0
        for i in range(0, len(res), 3):
            a = res[i : i + 3]
            if len(a) >= 2:
                ans += a[0] + a[1]
            else:
                ans += a[0]
        return ans
