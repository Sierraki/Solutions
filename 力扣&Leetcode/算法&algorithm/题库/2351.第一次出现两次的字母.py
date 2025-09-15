class Solution:
    def repeatedCharacter(self, s: str) -> str:
        cnt = Counter()
        for i in s:
            cnt[i] += 1
            if cnt[i] == 2:
                return i
