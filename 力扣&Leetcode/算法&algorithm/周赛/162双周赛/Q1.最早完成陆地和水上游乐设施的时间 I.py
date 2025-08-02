class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        wn = len(waterDuration)
        ln = len(landDuration)
        ans = float("inf")
        for i in range(wn):
            for j in range(ln):
                # 先水后陆地
                if waterStartTime[i] <= landStartTime[j]:
                    # 要等
                    if waterStartTime[i] + waterDuration[i] <= landStartTime[j]:
                        ans = min(ans, landStartTime[j] + landDuration[j])
                    # 不要等
                    else:
                        ans = min(
                            ans, waterStartTime[i] + waterDuration[i] + landDuration[j]
                        )
                # 先陆地后水
                else:
                    # 要等
                    if landStartTime[j] + landDuration[j] <= waterStartTime[i]:
                        ans = min(ans, waterStartTime[i] + waterDuration[i])
                    # 不要等
                    else:
                        ans = min(
                            ans, landStartTime[j] + landDuration[j] + waterDuration[i]
                        )
        return ans
