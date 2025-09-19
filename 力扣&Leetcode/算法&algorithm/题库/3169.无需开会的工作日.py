class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # 合并区间
        meetings.sort()
        res = [meetings[0]]
        for i in meetings[1:]:
            if i[0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(i[1], res[-1][1])]
            else:
                res.append(i)
        ans = 0
        for i in range(1, len(res)):
            ans += res[i][0] - res[i - 1][1] - 1
        ans += res[0][0] - 1 + days - res[-1][1]
        return ans
