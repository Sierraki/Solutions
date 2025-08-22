class Solution:
    def countEven(self, num: int) -> int:
        def fun(num: int) -> bool:
            c = 0
            for i in str(num):
                c += int(i)
            if c % 2 == 0:
                return True
            return False

        ans = 0
        for i in range(1, num + 1):
            if fun(i):
                ans += 1
        return ans
