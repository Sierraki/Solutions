class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        for i in range(1, floor(sqrt(max(a, b)))):
            if a % i == 0 and b % i == 0:
                ans += 1
        return ans


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        c, ans = gcd(a, b), 0
        x = 1
        while x * x <= c:
            if c % x == 0:
                ans += 1
                if x * x != c:
                    ans += 1
            x += 1
        return ans
