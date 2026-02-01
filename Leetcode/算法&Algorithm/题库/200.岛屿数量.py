# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(x, y):
            tar = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for i, j in tar:
                if 0 <= x + i < n and 0 <= y + j < m:
                    if grid[x + i][y + j] == "1":
                        grid[x + i][y + j] = "x"
                        dfs(x + i, y + j)

        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    grid[i][j] = "x"
                    cnt += 1
                    dfs(i, j)
        return cnt

# BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    cnt += 1
                    grid[i][j] = "0"
                    queue = collections.deque([(i, j)])
                    while queue:
                        cur_x, cur_y = queue.popleft()
                        tar = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                        for dx, dy in tar:
                            nx, ny = cur_x + dx, cur_y + dy
                            if 0 <= nx < n and 0 <= ny < m:
                                if grid[nx][ny] == "1":
                                    grid[nx][ny] = "0"
                                    queue.append((nx, ny))
        return cnt
