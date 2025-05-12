class Solution:
    def A(self, s: str):
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                if right - left <= 0:
                    return True
            else:
                sta = self.A(s[left + 1 : right + 1])
                stb = self.A(s[left:right])
                if not sta and not stb:
                    return False
                else:
                    return True
