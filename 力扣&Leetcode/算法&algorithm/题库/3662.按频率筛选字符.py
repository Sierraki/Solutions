class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        cnt = Counter(s)
        tar = set([i for i, j in cnt.items() if j < k])
        ans = ""
        for i in s:
            if i in tar:
                ans += i
        return ans
