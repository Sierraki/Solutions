class Solution:
    def digitCount(self, num: str) -> bool:
        cnt = Counter(map(int, num))
        for idx, i in enumerate(str(num)):
            if int(i) != cnt[idx]:
                return False
        return True
