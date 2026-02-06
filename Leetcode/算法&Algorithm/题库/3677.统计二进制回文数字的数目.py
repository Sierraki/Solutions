class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0:
            return 1
        s = bin(n)[2:]
        L = len(s)
        cnt = 0
        for k in range(1, L):
            m = (k + 1) // 2
            cnt += 2 ** (m - 1)
        m = (L + 1) // 2
        res1 = s[:m]
        res2 = int(res1, 2)
        cnt += res2 - (2 ** (m - 1))
        ans1 = L // 2
        ans2 = res1[:ans1][::-1]
        ans = res1 + ans2
        if ans <= s:
            cnt += 1
        return cnt + 1
