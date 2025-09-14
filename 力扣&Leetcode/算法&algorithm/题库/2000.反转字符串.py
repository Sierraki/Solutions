class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                p1 = word[: i + 1]
                p2 = word[i + 1 :]
                word = p1[::-1] + p2
                break
        return word
