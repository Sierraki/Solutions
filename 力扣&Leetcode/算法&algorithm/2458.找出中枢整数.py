class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        res = [i for i in range(1, 1 + n)]
        res1 = []
        s = 0
        for i in res:
            s += i
            res1.append(s)
        cnt = res1[-1]
        ans = -1
        for i in range(len(res1)):
            if res1[i - 1] == cnt - res1[i]:
                ans = i + 1
        return ans
