class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        cnt = 0
        while target != startValue:
            if target > startValue:
                if target % 2 == 0:
                    target = target // 2
                else:
                    target += 1
                cnt += 1
            else:
                return cnt + startValue - target
        return cnt
