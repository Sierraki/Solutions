class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        ans = ""
        for i in range(len(words)):
            ans += words[i][0]
        return ans == s
