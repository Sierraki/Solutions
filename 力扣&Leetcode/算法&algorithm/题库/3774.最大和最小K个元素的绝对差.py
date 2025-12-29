class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        p1 = nums[:k]
        nums.sort(reverse=True)
        p2 = nums[:k]
        return abs(sum(p1) - sum(p2))
