class Solution:
    def scoreBalance(self, s: str) -> bool:
        ans = Counter()
        cnt = 0
        for i in s:
            cnt += ord(i) - 96
            ans[cnt] += 1
        if cnt % 2 != 0:
            return False
        return cnt // 2 in ans
