class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for j in cnt.values():
            if j > 2:
                return False
        return True
