class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        tar = [i for i, j in cnt.items() if j <= 1]
        ans = -1
        for idx, i in enumerate(s):
            if i in tar:
                ans = idx
                break
        return ans
