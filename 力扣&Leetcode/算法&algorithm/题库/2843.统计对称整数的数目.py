class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def fun(x: int):
            num = str(x)
            if len(num) % 2 == 1:
                return False
            else:
                n = len(num) // 2
                return sum(map(int, num[:n])) == sum(map(int, num[n:]))

        ans = 0
        for i in range(low, high + 1):
            if fun(i):
                ans += 1
        return ans
