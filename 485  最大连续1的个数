class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = 0  # 最大值
        b = 0  # 当前值
        for i in nums:
            if i == 1:
                b = b + 1
                if b > a:
                    a = b
            if i != 1:
                b = 0
        return a
