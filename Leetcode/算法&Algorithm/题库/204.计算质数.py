class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        mx = n
        primes = []
        res = [True] * mx
        for i in range(2, mx):
            if res[i] == True:
                primes.append(i)
                for j in range(i * i, mx, i):
                    res[j] = False
        return len(primes)
