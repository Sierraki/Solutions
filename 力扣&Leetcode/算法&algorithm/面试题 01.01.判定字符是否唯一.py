class Solution:
    def isUnique(self, astr: str) -> bool:
        cnt = Counter()
        for i in astr:
            if i not in cnt:
                cnt[i] += 1
            else:
                return False
        return True
