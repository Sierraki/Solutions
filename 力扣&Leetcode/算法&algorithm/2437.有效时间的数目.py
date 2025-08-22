class Solution:
    def countTime(self, time: str) -> int:
        a = time[0]
        b = time[1]
        c = time[3]
        d = time[4]
        ans1 = ans2 = 1
        # hours
        if a == "?":
            if b == "?":
                # ??
                ans1 = 24
            else:
                # ?x
                if int(b) <= 3:
                    ans1 = 3
                else:
                    ans1 = 2
        else:
            if b == "?":
                # x?
                if int(a) <= 1:
                    ans1 = 10
                else:
                    ans1 = 4
        if c == "?":
            if d == "?":
                # ??
                ans2 = 60
            else:
                # ?x
                ans2 = 6
        else:
            if d == "?":
                # x?
                ans2 = 10
        return ans1 * ans2
