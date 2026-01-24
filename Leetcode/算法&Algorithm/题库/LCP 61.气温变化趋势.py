class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        res1 = []
        res2 = []
        for i in range(1, len(temperatureA)):
            if temperatureA[i - 1] > temperatureA[i]:
                res1.append(0)
            elif temperatureA[i - 1] < temperatureA[i]:
                res1.append(1)
            else:
                res1.append(2)
        for i in range(1, len(temperatureA)):
            if temperatureB[i - 1] > temperatureB[i]:
                res2.append(0)
            elif temperatureB[i - 1] < temperatureB[i]:
                res2.append(1)
            else:
                res2.append(2)
        cnt = 0
        mx = 0
        for i in range(len(res1)):
            if res1[i] == res2[i]:
                cnt += 1
            else:
                cnt = 0
            mx = max(mx, cnt)
        return mx
