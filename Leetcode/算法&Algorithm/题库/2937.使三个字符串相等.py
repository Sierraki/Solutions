class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n = min(len(s1), len(s2), len(s3))
        s11 = s1[:n]
        s22 = s2[:n]
        s33 = s3[:n]
        if s11 == s22 == s33:
            return len(s1 + s2 + s3) - 3 * n
        else:
            if not (s1[0] == s2[0] == s3[0]):
                return -1
            else:
                for i in range(n):
                    if not (s1[i] == s2[i] == s3[i]):
                        return len(s1 + s2 + s3) - 3 * i
# 慢一点但简洁
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n = min(len(s1), len(s2), len(s3))
        if not (s1[0] == s2[0] == s3[0]):
            return -1
        for i in range(n + 1):
            if i == n or (not (s1[i] == s2[i] == s3[i])):
                return len(s1 + s2 + s3) - 3 * i
