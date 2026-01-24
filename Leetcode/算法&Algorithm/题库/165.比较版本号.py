class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        res1 = version1.split(".")
        res2 = version2.split(".")
        n = max(len(res1), len(res2))
        if len(res1) < n:
            for _ in range(n - len(res1)):
                res1.append("0")
        elif len(res2) < n:
            for _ in range(n - len(res2)):
                res2.append("0")
        for i in range(n):
            if int(res1[i]) > int(res2[i]):
                return 1
            if int(res1[i]) < int(res2[i]):
                return -1
        return 0
