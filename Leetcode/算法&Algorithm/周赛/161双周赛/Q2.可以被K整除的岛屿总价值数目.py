class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        # 访问
        visited = [[False] * n for _ in range(m)]
        cnt = 0
        row = [-1, 1, 0, 0]
        col = [0, 0, -1, 1]
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and not visited[r][c]:
                    curv = 0
                    q = deque()
                    q.append((r, c))
                    visited[r][c] = True
                    while q:
                        curr_r, curr_c = q.popleft()
                        curv += grid[curr_r][curr_c]
                        for i in range(4):
                            nr, nc = curr_r + row[i], curr_c + col[i]
                            if (
                                0 <= nr < m
                                and 0 <= nc < n
                                and grid[nr][nc] > 0
                                and not visited[nr][nc]
                            ):
                                q.append((nr, nc))
                                visited[nr][nc] = True
                    if curv % k == 0:
                        cnt += 1
        return cnt
