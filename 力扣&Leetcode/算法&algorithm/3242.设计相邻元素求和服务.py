class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.find = defaultdict(list)
        for i in range(self.m):
            for j in range(self.n):
                self.find[grid[i][j]] = [i, j]

    def fun(self, lo: list) -> bool:
        return 0 <= lo[0] < self.m and 0 <= lo[1] < self.n

    def adjacentSum(self, value: int) -> int:
        # 十
        a = self.find[value][0]
        b = self.find[value][1]
        res = [[a - 1, b], [a, b + 1], [a + 1, b], [a, b - 1]]
        ans = 0
        for i in res:
            if self.fun(i):
                ans += self.grid[i[0]][i[1]]
        return ans

    def diagonalSum(self, value: int) -> int:
        a = self.find[value][0]
        b = self.find[value][1]
        res = [[a - 1, b - 1], [a - 1, b + 1], [a + 1, b + 1], [a + 1, b - 1]]
        ans = 0
        for i in res:
            if self.fun(i):
                ans += self.grid[i[0]][i[1]]
        return ans


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
