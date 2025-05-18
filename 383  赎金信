class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)
        s = True
        for i in a:
            if a[i] > b[i]:
                s = False
        return s
