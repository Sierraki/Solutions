class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a = []
        b = []
        for i in nums:
            if i % 2 == 0:
                a.append(i)
            else:
                b.append(i)
        return a + b
