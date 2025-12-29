class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        res = [int((bin(i)[2:])[::-1], 2) for i in nums]
        res1 = list(zip(nums, res))
        res1.sort(key=lambda x: (x[1], x[0]))
        return [i[0] for i in res1]
