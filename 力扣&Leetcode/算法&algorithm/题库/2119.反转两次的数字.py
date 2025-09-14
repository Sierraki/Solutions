class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        nums = str(num)
        if nums != "0" and nums[-1] == "0":
            return False
        else:
            return True
