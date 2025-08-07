class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def fun(n: int) -> bool:
            if n <= 1:
                return False
            elif n == 2:
                return True
            elif n % 2 == 0:
                return False
            else:
                for i in range(3, int(n**0.5) + 1, 2):
                    if n % i == 0:
                        return False
            return True

        cnt = Counter(nums)
        for i in cnt.values():
            if fun(i):
                return True
        return False
