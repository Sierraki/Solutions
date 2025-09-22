class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        l = t = float("inf")
        r = d = -float("inf")
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    l = min(l, j)
                    r = max(r, j)
                    d = i
                    if t == float("inf"):
                        t = i
        return (r - l + 1) * (d - t + 1)
