class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        def fun1(n):
            dp = [0] * (n + 1)
            for i in range(1, n + 1):
                if i <= 2:
                    dp[i] = i
                elif i == 3:
                    dp[i] = 4
                else:
                    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
            return dp[-1]

        def fun2(n):
            dp = [0] * (n + 1)
            for i in range(1, n + 1):
                if i <= 2:
                    dp[i] = i
                elif i == 3:
                    dp[i] = 4
                elif i == 4:
                    dp[i] = 7 + 1
                else:
                    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]
            return dp[-1]

        pin = 0
        res = []
        mx1 = mx2 = 0
        for i, j in enumerate(pressedKeys):
            if j != pressedKeys[pin]:
                res.append(pressedKeys[pin:i])
                if pressedKeys[pin] in "234568":
                    mx1 = max(mx1, i - pin)
                else:
                    mx2 = max(mx2, i - pin)
                pin = i
        if pin == 0 or pressedKeys[pin] != res[-1][-1]:
            res.append(pressedKeys[pin:])
            if pressedKeys[pin] in "234568":
                mx1 = max(mx1, len(pressedKeys) - pin)
            else:
                mx2 = max(mx2, len(pressedKeys) - pin)
        fun1(mx1)
        fun2(mx2)
        ans = 1
        mod = 10**9 + 7
        for i in res:
            if i[0] in "234568":
                ans = ans * fun1(len(i)) % mod
            else:
                ans = ans * fun2(len(i)) % mod
        return ans
