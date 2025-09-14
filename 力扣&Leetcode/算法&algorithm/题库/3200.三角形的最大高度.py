class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def fun(x1: int, x2: int) -> int:
            # 1 start
            a = floor(sqrt(x1))
            # 2 start
            b = (-1 + sqrt(1 + 4 * x2)) // 2
            # return [a, b]
            if a == 0 or b == 0:
                return 1
            if a == b:
                ans = a + b
            elif a > b:
                ans = 2 * b + 1
            else:
                ans = 2 * a
            return int(ans)

        return max(fun(red, blue), fun(blue, red))
