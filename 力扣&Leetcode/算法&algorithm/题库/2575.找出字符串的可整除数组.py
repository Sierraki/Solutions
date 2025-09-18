class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = [0] * len(word)
        ans = int(word[0])
        if ans % m == 0:
            res[0] = 1
        ans = ans % m
        for i in range(1, len(word)):
            ans = ans * 10 + int(word[i])
            ans = ans % m
            if ans == 0:
                res[i] = 1
        return res
