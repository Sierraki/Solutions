class Solution:
    def reverseByType(self, s: str) -> str:

        res1 = []
        res2 = []
        for i in s:
            if i.isalpha():
                res1.append(i)
            else:
                res2.append(i)
        res1 = res1[::-1]
        res2 = res2[::-1]
        p1 = 0
        p2 = 0
        res = ""
        for i in s:
            if i.isalpha():
                res += res1[p1]
                p1 += 1
            else:
                res += res2[p2]
                p2 += 1
        return res
