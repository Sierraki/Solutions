class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        c = 0
        swap = False
        for i, j in cnt.items():
            if j % 2 == 0:
                c += j
            else:
                c += j - 1
                swap = True
        if swap:
            return c + 1
        return c
