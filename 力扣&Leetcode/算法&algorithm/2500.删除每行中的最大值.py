class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i] = sorted(grid[i])
        res = 0
        while len(grid[0]) >= 1:
            mx = 0
            for i in grid:
                mx = max(mx, i[-1])
                i.pop(-1)
            res += mx
        return res
