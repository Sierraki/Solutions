class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        check = dict(zip(keyboard, [i for i in range(26)]))
        ans = 0
        for i in range(len(word)):
            if i == 0:
                ans += check[word[i]]
            else:
                ans += abs(check[word[i]] - check[word[i - 1]])
        return ans
