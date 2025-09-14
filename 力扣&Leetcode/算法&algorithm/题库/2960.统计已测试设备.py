class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        def fun(a: list, x: int) -> list:
            p1 = a[:x]
            p2 = a[x:]
            for i in range(len(p2)):
                if p2[i] > 0:
                    p2[i] -= 1
            return p1 + p2

        cnt = 0
        pin = 0
        while pin < len(batteryPercentages):
            if batteryPercentages[pin] > 0:
                batteryPercentages = fun(batteryPercentages, pin + 1)
                cnt += 1
            pin += 1
        return cnt
