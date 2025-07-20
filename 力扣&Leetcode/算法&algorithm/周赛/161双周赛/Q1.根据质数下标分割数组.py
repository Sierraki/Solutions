class Solution:
    def splitArray(self, nums: List[int]) -> int:
        def check(a: int) -> bool:
            if a == 1:
                return False
            if a == 0:
                return False
            for i in range(2, floor(sqrt(a)) + 1):
                if a % i == 0:
                    return False
            return True

        ans = 0
        for idx, i in enumerate(nums):
            if check(idx):
                ans += i
            else:
                ans -= i
        return abs(ans)
