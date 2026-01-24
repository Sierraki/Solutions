class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = right = 0
        while right < len(s):
            if right == len(s) - 1 or s[right + 1] == " ":
                lc = right
                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                right = left = lc + 2
            else:
                right += 1
        s.reverse()
