class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        nums = s.split("0")
        return len([i for i in nums if i != ""]) <= 1
