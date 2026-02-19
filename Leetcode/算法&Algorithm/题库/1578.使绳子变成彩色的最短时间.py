class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        ans = 0
        max_time = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                ans += min(max_time, neededTime[i])
                max_time = max(max_time, neededTime[i])
            else:
                max_time = neededTime[i]
        return ans
