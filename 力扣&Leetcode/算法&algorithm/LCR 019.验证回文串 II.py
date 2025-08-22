class Solution(object):
    def validPalindrome(self, s):
        def fun(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return fun(s[l + 1 : r + 1]) or fun(s[l:r])
            l += 1
            r -= 1
        return True
