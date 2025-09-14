class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = [i for i in s]
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if ord(s[left]) < ord(s[right]):
                    s[right] = s[left]
                else:
                    s[left] = s[right]
            left += 1
            right -= 1
        return "".join(s)
