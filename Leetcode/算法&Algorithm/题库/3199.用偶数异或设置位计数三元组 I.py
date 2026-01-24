class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def fun1(num=int) -> bool:
            return bin(num)[2:].count("1") % 2 == 0

        def fun2(nums=list) -> int:
            ans = nums[0]
            for i in range(1, len(nums)):
                ans ^= nums[i]
            return ans

        ans = 0
        for i in range(len(a)):
            for j in range(len(b)):
                for k in range(len(c)):
                    if fun1(fun2([a[i], b[j], c[k]])):
                        ans += 1
        return ans
