class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        tar = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        nums = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    nums.append([i, j])
                if grid[i][j] == 1:
                    fresh += 1
        cnt = 0
        while nums and fresh > 0:
            size = len(nums)
            for _ in range(size):
                x, y = nums.popleft()
                if grid[x][y] == 2:
                    for i, j in tar:
                        if 0 <= x + i < m and 0 <= y + j < n:
                            if grid[x + i][y + j] == 1:
                                nums.append([x + i, y + j])
                                grid[x + i][y + j] = 2
                                fresh -= 1
            cnt += 1
        return cnt if fresh == 0 else -1
