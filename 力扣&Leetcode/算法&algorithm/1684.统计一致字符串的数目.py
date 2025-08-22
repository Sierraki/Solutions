class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        for i in range(len(words)):
            words[i] = Counter(words[i])
        ans = 0

        def fun(a: str, b=dict) -> bool:
            res = [i for i in b.keys()]
            b1 = set(res)
            b2 = [i for i in res if i in a]
            return len(b1) == len(b2)

        for i in words:
            if fun(allowed, i):
                ans += 1
        return ans
