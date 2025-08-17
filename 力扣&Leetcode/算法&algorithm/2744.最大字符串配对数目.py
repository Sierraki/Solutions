class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        cnt = set()
        ans = 0
        for i in words:
            if i[::-1] in cnt:
                ans += 1
            cnt.add(i)
        return ans
