class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        def is_zhishu(intt):
            if intt <= 1:
                return False
            if intt == 2:
                return True
            if intt % 2 == 0:
                return False
            for i in range(3, int(intt**0.5) + 1, 2):
                if intt % i == 0:
                    return False
            else:
                return True
        a = []
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                num = int(s[i:j])
                if is_zhishu(num) == True:
                    a.append(num)
        l = len(a)
        a = list(set(a))
        if l <= 3:
            return sum(a)
        else:
            a.sort(reverse=True)
            a = a[:3]
            return sum(a)
