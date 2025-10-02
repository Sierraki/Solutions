# items[0][0] 为容量，items[0][1]为价值
items = [[2, 3], [3, 4], [4, 5], [5, 8], [1, 2]]
capacity = 7
dp = [[0] * (capacity + 1) for _ in range(len(items))]


for i in range(len(items)):
    for j in range(capacity + 1):
        if i > 0:
            dp[i][j] = dp[i - 1][j]
        if j >= items[i][0]:
            dp[i][j] = max(dp[i][j], dp[i][j - items[i][0]] + items[i][1])
print(dp)
