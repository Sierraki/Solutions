class Solution:
    def averageValue(self, nums: List[int]) -> int:
        cur = cnt = 0
        for i in nums:
            if i % 6 == 0:
                cur += i
                cnt += 1
        if cnt == 0:
            return 0
        else:
            return cur // cnt
