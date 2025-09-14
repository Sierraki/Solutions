class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a = []
        b = []
        for idx, i in enumerate(nums):
            if idx == 0:
                a.append(i)
            elif idx == 1:
                b.append(i)
            elif idx > 1:
                if a[-1] > b[-1]:
                    a.append(i)
                else:
                    b.append(i)
        return a + b
