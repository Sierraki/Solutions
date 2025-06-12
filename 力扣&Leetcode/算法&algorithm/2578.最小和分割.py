class Solution:
    def splitNum(self, num: int) -> int:
        nums = [i for i in str(num)]
        nums.sort()
        n1 = []
        n2 = []
        for idx, i in enumerate(nums):
            if idx % 2 == 0:
                n1.append(i)
            else:
                n2.append(i)
        n1 = "".join(n1)
        n2 = "".join(n2)
        return int(n1) + int(n2)
