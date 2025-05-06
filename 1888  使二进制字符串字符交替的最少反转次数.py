class Solution:
    def minFlips(self, s: str) -> int:
        s = [int(i) for i in s]
        k = n = len(s)  # 窗口长度
        s += s
        t1 = [1, 0] * k
        # print(s)
        # print(t1)
        a = []
        for i in range(2 * n):
            if s[i] == t1[i]:
                a.append(-1)
            else:
                a.append(1)
        # print(a)
        cur = sum(a[:k])
        mx = abs((sum(a[:k])))

        for i in range(k, 2 * n):
            cur += a[i] - a[i - k]
            mx = max(mx, abs(cur))
        # print(mx)
        b = (k - mx) / 2
        res = min(b, k - b)
        return int(res)
