# items[0][0] 为容量，items[0][1]为价值
items = [[2, 3], [3, 4], [4, 5], [5, 8], [1, 2]]
capacity = 7
dp = [[0] * (capacity + 1) for _ in range(len(items))]
# 处理第一行
for i in range(items[0][0], capacity + 1):
    dp[0][i] = items[0][1]

for i in range(1, len(dp)):
    for j in range(capacity + 1):
        # 上一个，加上当前值还有空余再加上一个行的剩余容量最佳
        dp[i][j] = dp[i - 1][j]
        # 选当前
        if j - items[i][0] >= 0:
            dp[i][j] = max(dp[i][j], items[i][1] + dp[i - 1][j - items[i][0]])
print(dp)
