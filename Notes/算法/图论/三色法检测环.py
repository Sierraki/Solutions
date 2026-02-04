# 0 未遍历
# 1 已经遍历一次
# 2 安全
n = 10
vis = [0] * n
nums = [[1, 0]]


def dfs(cur):
    if vis[cur] > 0:
        return vis[cur] == 2
    vis[cur] = 1
    for i in nums[cur]:
        if not dfs(i):
            return False
    vis[cur] = 2
    return True
