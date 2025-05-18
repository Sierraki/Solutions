class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        cnt = 0
        while cnt < n:
            nums.append(cnt * 2 + start)
            cnt += 1
        a = 0
        for i in nums:
            a = a ^ i
        return a
