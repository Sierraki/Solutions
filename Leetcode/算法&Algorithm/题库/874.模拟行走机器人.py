class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        x, y = 0, 0
        mx = 0
        for cmd in commands:
            if cmd == -2:
                d = (d + 3) % 4
            elif cmd == -1:
                d = (d + 1) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obstacle_set:
                        break
                    x, y = nx, ny
                mx = max(mx, x * x + y * y)
        return mx
