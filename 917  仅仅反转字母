class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        a = [i for i in s]
        b = a.copy()  # 处理过的
        l = 0
        n = len(s)
        for i in range(n):
            if s[i].isalpha():
                b[l] = " "
            else:
                b[l] = s[i]
            l += 1
        r = n - 1
        ss = []
        while r >= 0:
            if s[r].isalpha():
                ss.append(s[r])
            r -= 1
        t = 0
        d = 0
        while d < len(ss):
            if b[t] == " ":
                b[t] = ss[d]
                t += 1
                d += 1
            else:
                t += 1
        bb = "".join(b)
        return bb
