class Solution:
    def maximumTime(self, time: str) -> str:
        p1 = [time[0], time[1]]
        p2 = [time[3], time[4]]
        # print(p1, p2)
        # ??
        if p1 == ["?", "?"]:
            p1 = "23"
        # ?x
        elif p1[0] == "?":
            if int(p1[1]) <= 3:
                p1[0] = "2"
            else:
                p1[0] = "1"
        # ?x
        elif p1[1] == "?":
            if int(p1[0]) == 2:
                p1[1] = "3"
            else:
                p1[1] = "9"
        p1 = "".join(p1)
        # ??
        if p2 == ["?", "?"]:
            p2 = "59"
        # ?x
        elif p2[0] == "?":
            p2[0] = "5"
        # x?
        elif p2[1] == "?":
            p2[1] = "9"
        p2 = "".join(p2)
        ans = p1 + ":" + p2
        return ans
