import sys

input = sys.stdin.readline
n = int(input())
grid = [res1, res2, res3] = [list(map(int, input().split())) for _ in range(3)]
dp = [[0] * n for _ in range(3)]
dp[0][0] = grid[0][0]
for i in range(3):
    for j in range(n):
        if i <= j:
            if i == 0 and j >= 1:
                dp[i][j] = grid[i][j] + dp[i][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1]) + grid[i][j]
print(dp[-1][-1])
