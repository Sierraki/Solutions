class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def fun(s1=str, s2=str) -> bool:
            if len(s2) < len(s1):
                return False
            else:
                n = len(s1)
                return s2[:n] == s1 and s2[len(s2) - n :] == s1

        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if fun(words[i], words[j]):
                    ans += 1
        return ans
