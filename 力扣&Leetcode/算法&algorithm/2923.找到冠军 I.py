class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res.append([i, j])
        ans = res[0]
        for i in res:
            if i[1] == ans[0]:
                ans = i
        return ans[0]


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for idx, i in enumerate(grid):
            if sum(i) == len(grid[0]) - 1:
                return idx
