class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        def fun(nums=list) -> list:
            s = 0
            res = []
            for i in nums:
                s += i
                res.append(s)
            return res

        nums = [1] * n
        ans = 1
        for _ in range(k):
            nums = fun(nums)
            ans = nums[-1] % (10**9 + 7)
        return ans
