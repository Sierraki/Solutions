class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = float("inf")
        for i, j in tasks:
            ans = min(ans, i + j)
        return ans