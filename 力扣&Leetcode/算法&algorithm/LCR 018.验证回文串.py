class Solution(object):
    def isPalindrome(self, s):
        s = [i.lower() for i in s if i.isalpha() or i.isalnum()]
        res = "".join(s)
        l, r = 0, len(res) - 1
        while l < r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        return True
