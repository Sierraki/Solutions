class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for i in patterns:
            if i in word:
                ans += 1
        return ans
