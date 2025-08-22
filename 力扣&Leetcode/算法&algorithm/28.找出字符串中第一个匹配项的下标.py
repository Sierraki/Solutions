class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ha = len(haystack)
        ne = len(needle)
        for i in range(ha - ne + 1):
            if haystack[i : i + ne] == needle:
                return i
        else:
            return -1

# KMP
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)
        mx = 0
        n = len(needle)
        for i in range(1, n):
            while mx > 0 and needle[i] != needle[mx]:
                mx = lps[mx - 1]
            if needle[i] == needle[mx]:
                mx += 1
            lps[i] = mx
        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                j += 1
                i += 1
            if j == n:
                return i - n
            elif i < len(haystack) and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1
