import sys


def fun(grid):
    for i in range(n - 1):
        for j in range(n - 1):
            if grid[i][j] == 1:
                if not (grid[i + 1][j] == 1 or grid[i][j + 1] == 1):
                    return "NO"
    return "YES"


input = sys.stdin.readline
size = int(input())
for _ in range(size):
    n = int(input())
    grid = [list(map(int, input().strip())) for _ in range(n)]
    print(fun(grid))
