class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        t = []
        for idx, i in enumerate(nums):
            if i == target:
                t.append(idx)
        cur = 0
        big = abs(t[0] - start)

        for i in t:
            cur = abs(i - start)
            if cur < big:
                big = cur

        return big
