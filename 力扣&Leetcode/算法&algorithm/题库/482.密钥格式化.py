class Solution(object):
    def licenseKeyFormatting(self, s, k):
        res1 = [i.upper() for i in s if i != "-"]
        n = len(res1)
        lap = n % k
        if lap > 0:
            p1 = "".join(res1[:lap])
            res1 = res1[lap:]
        else:
            p1 = ""
        p2 = ""
        for i in range(0, len(res1), k):
            ans = "".join(res1[i : i + k])
            p2 += ans + "-"
        if p1 == "":
            res = p1 + p2
        else:
            res = p1 + "-" + p2
        return res[:-1]
