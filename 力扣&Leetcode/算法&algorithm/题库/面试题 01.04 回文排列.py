class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt = Counter(s)
        check = 0
        for i in cnt.values():
            if i % 2 == 1:
                check += 1
            if check > 1:
                return False
        return True
