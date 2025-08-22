class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        cnt = {i: 1 for i in brokenLetters}
        ans = len(text.split())
        for i in text.split():
            for j in i:
                if j in cnt:
                    ans -= 1
                    break
        return ans
