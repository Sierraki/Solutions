class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for i in cnt.values():
            if i % 2 != 0:
                return False
        return True
