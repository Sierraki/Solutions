class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        up = Counter([i for i, j in intervals])
        down = Counter([j for i, j in intervals])
        n = 0
        for i in intervals:
            n = max(n, i[1])
        ans = 0
        cur = 0
        for i in range(n):
            cur += up[i] - down[i]
            ans = max(ans, cur)
        return ans
