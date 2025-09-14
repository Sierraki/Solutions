class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        left = len(s) - 1
        cnt = 0
        while left >= 0:
            if s[left].isalpha():
                cnt += 1
            left -= 1
            if cnt != 0 and s[left] == " ":
                break
        return cnt
