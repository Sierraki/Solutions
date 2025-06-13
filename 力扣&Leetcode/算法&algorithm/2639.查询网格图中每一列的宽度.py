class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(grid[0])):
            mx = 0
            for j in grid:
                mx = max(mx, len(str(j[i])))
            res.append(mx)
        return res
