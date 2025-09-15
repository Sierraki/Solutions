class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [i for i in s]
        check = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        left, right = 0, len(s) - 1
        while left < right:
            while s[left] not in check:
                if left >= right:
                    break
                left += 1
            while s[right] not in check:
                if left >= right:
                    break
                right -= 1
            if left >= right:
                break
            if s[left] in check and s[right] in check:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)
