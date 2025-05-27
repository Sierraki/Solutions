class Solution:
    def removeVowels(self, s: str) -> str:
        t = "aeiou"
        s = [i for i in s if i not in t]
        return "".join(s)
