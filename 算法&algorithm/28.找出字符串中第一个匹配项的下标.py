class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ha = len(haystack)
        ne = len(needle)
        for i in range(ha - ne + 1):
            if haystack[i : i + ne] == needle:
                return i
                break
        else:
            return -1
