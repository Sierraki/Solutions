class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        adj = [[] for _ in range(n)]
        for i, j in relation:
            adj[i].append(j)
        nums = deque([0])
        for _ in range(k):
            size = len(nums)
            for _ in range(size):
                cur = nums.popleft()
                for i in adj[cur]:
                    nums.append(i)
        cnt = 0
        for i in nums:
            if i == n - 1:
                cnt += 1
        return cnt
