class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        def check(num):
            ans = 1
            for i in range(1, num + 1):
                ans = ans * i
            return ans

        ans = 0
        for i in str(n):
            ans += check(int(i))
        return Counter(list(str(n))) == Counter(list(str(ans)))
