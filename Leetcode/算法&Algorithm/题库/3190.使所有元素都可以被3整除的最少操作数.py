class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            ans1 = i // 3
            ans2 = ans1 + 1
            res += min(abs(ans2 * 3 - i), abs(ans1 * 3 - i))
        return res
