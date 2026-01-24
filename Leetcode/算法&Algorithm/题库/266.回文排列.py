class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt = Counter(s)
        c = 0
        for i in cnt.values():
            if i % 2 == 1:
                c += 1
            if c > 1:
                return False
        return True
