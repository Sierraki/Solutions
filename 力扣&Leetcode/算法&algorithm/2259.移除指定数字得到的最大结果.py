class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        nums = [i for i in number]
        res = -float("inf")
        for idx, i in enumerate(nums):
            if i == digit:
                cop = nums.copy()
                del cop[idx]
                res = max(res, int("".join(cop)))
        return str(res)
