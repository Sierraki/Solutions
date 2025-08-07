class Solution:
    def numberCount(self, a: int, b: int) -> int:
        def fun(x: int) -> bool:
            return len(str(x)) == len(set(str(x)))

        ans = 0
        for i in range(a, b + 1):
            if fun(i):
                ans += 1
        return ans
