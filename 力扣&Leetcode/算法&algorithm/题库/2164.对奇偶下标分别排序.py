class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        j = []
        o = []
        for idx, i in enumerate(nums):
            if idx % 2 == 0:
                o.append(i)
            else:
                j.append(i)
        j.sort(reverse=True)
        o.sort()
        a = []
        for i in range(len(j)):
            a.append(o[i])
            a.append(j[i])
        if len(o) == len(j):
            return a
        else:
            a.append(o[-1])
            return a
