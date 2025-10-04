class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # 普通
        def is_prime(n: int) -> bool:
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

        cnt = 0
        for i in range(1, n + 1):
            if is_prime(i):
                cnt += 1

        # 排列
        def fun(a=int):
            ans = 1
            for i in range(1, a + 1):
                ans *= i
            return ans

        ans = (fun(cnt) * fun(n - cnt)) % (10**9 + 7)
        return ans
