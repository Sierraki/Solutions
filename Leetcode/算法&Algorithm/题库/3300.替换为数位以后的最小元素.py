class Solution:
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)
        list1 = []
        for i in range(n):
            a = str(nums[i])
            summ = 0
            for j in a:
                summ = summ + int(j)
            list1.append(summ)
        return min(list1)
