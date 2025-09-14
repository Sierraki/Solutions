class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        for i in range(0, len(s), k):
            res.append(s[i : i + k])
        if len(res[-1]) < k:
            a = [fill] * k
            for i in range(len(res[-1])):
                a[i] = res[-1][i]
            res[-1] = "".join(a)
        return res
