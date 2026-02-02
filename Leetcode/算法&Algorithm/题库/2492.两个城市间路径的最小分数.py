class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        nums = [[] for _ in range(n + 1)]
        for i, j, k in roads:
            nums[i].append((j, k))
            nums[j].append((i, k))
        res = deque([1])
        cost = float("inf")
        vis = [False] * (n + 1)
        while res:
            cur = res.popleft()
            if not vis[cur]:
                vis[cur] = True
                for i in nums[cur]:
                    cost = min(cost, i[1])
                    res.append(i[0])
        return cost
