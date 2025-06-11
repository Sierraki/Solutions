class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        s = words + words + words
        res = []
        for idx, i in enumerate(s):
            if i == target:
                res.append(idx)
        if not res:
            return -1
        mi = float("inf")
        for i in res:
            mi = min(mi, abs(n + startIndex - i))
        return mi
