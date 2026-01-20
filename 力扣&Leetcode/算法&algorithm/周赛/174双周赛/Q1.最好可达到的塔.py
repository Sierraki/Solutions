class Solution:
    def bestTower(
        self, towers: List[List[int]], center: List[int], radius: int
    ) -> List[int]:
        res = []
        mx = -float("inf")
        for i, j, k in towers:
            if abs(i - center[0]) + abs(j - center[1]) <= radius:
                if k >= mx:
                    res.append([i, j, k])
                    mx = k
        res.sort(key=lambda x: (-x[2], x[0], x[1]))
        if not res:
            return [-1, -1]
        ans = res[0]
        return [ans[0], ans[1]]
