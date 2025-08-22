class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        # 提取矩阵
        res = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            a = []
            for j in range(n):
                if x <= i < x + k and y <= j < y + k:
                    a.append(grid[i][j])
            if a:
                res.insert(0, a)
        ans = [j for i in res for j in i]
        pin = 0
        for i in range(m):
            for j in range(n):
                if x <= i < x + k and y <= j < y + k:
                    grid[i][j] = ans[pin]
                    pin += 1
        return grid


class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        l, r = x, x + k - 1
        while l < r:
            for j in range(y, y + k):
                grid[l][j], grid[r][j] = grid[r][j], grid[l][j]
            l += 1
            r -= 1
        return grid
