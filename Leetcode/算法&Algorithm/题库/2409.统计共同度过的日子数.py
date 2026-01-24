class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        res = []
        s = 0
        for i in mon:
            s += i
            res.append(s)
        res = {idx + 2: i for idx, i in enumerate(res)}
        res[1] = 0

        def fun(x: str) -> int:
            p1 = int(x[:2])
            p2 = int(x[3:])
            return res[p1] + p2

        a1 = fun(arriveAlice)
        a2 = fun(leaveAlice)
        b1 = fun(arriveBob)
        b2 = fun(leaveBob)
        ans = 0
        if a1 <= b1 <= a2 <= b2:
            ans = a2 - b1 + 1
        elif b1 <= a1 <= b2 <= a2:
            ans = b2 - a1 + 1
        elif b1 <= a1 <= a2 <= b2:
            ans = a2 - a1 + 1
        elif a1 <= b1 <= b2 <= a2:
            ans = b2 - b1 + 1
        return ans
