class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        cnt = 0
        for i in s:
            if i == "(":
                cnt += 1
            elif i == ")":
                cnt -= 1
            res.append(cnt)
        a = [[i, j] for i, j in list(zip(res, s))]
        for i in range(1, len(a)):
            if a[i][0] == 0 and a[i - 1][1] == "(":
                a[i - 1][0] = 0
            if a[i - 1][0] == 0 and a[i][1] == "(" and a[i - 1][1] == ")":
                a[i][0] = 0
        del a[0]
        a = [j for i, j in a if i != 0]
        return "".join(a)
