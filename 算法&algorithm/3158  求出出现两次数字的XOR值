class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        a = []
        b = 0
        for i in nums:
            if i not in a:
                a.append(i)
            else:
                b ^= i
        return b
