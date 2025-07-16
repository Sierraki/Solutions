class Solution:
    def getSmallestString(self, s: str) -> str:
        s = list(s)
        n = len(s)
        for i in range(1, n):
            # 判断是否为同一奇偶性
            if (int(s[i]) % 2) == (int(s[i - 1]) % 2):
                # 如果交换后字典序变小，就执行交换并返回结果
                if s[i] < s[i - 1]:
                    s[i], s[i - 1] = s[i - 1], s[i]
                    return "".join(s)
        # 如果没有符合条件的交换，返回原字符串
        return "".join(s)


class Solution:
    def getSmallestString(self, s: str) -> str:
        res = []

        for i in range(1, len(s)):
            if int(s[i]) % 2 == 0 and int(s[i - 1]) % 2 == 0:
                res.append([i - 1, i])
            elif int(s[i]) % 2 == 1 and int(s[i - 1]) % 2 == 1:
                res.append([i - 1, i])

        def fun(s: str, a: int, b: int) -> int:
            s = [i for i in s]
            s[a], s[b] = s[b], s[a]
            return int("".join(s))

        mx = float("inf")
        if not res:
            return s
        for i in res:
            mx = min(mx, fun(s, i[0], i[1]))
        mx = str(min(mx, int(s)))
        return mx.zfill(len(s))
