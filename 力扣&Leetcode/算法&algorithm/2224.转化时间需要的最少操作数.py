class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def fun(x: str) -> int:
            return int(x[:2]) * 60 + int(x[3:])

        dif = fun(correct) - fun(current)
        cnt = 0
        for step in [60, 15, 5, 1]:
            cnt += dif // step
            dif %= step
        return cnt
