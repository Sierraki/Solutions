class Solution:
    def minOperations(self, s: str) -> int:
        if len(set(s)) == 1 and s[0] == "a":
            return 0
        return 123 - min([ord(i) for i in s if i != "a"])
