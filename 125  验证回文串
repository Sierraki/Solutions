class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i.lower() for i in s if i.isalpha()or i.isalnum()])

        n = len(s)

        l = 0
        r = n - 1
        stat = True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                stat = False
                break
        return(stat)
