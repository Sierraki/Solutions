class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        tar = [i for i in nums if i % 2 == 0]
        if not tar:
            return 0
        ans = tar[0]
        for i in tar:
            ans = ans | i
        return ans
