class Solution:
    def calculate(self, s: str) -> int:
        def fx(x: int, y: int) -> int:
            return 2 * x + y

        def fy(x: int, y: int) -> int:
            return 2 * y + x

        x, y = 1, 0
        for i in s:
            if i == "A":
                x = fx(x, y)
            else:
                y = fy(x, y)
        return x + y
