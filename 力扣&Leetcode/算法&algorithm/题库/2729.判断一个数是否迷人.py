class Solution:
    def isFascinating(self, n: int) -> bool:
        nums = str(n) + str(2 * n) + str(3 * n)
        cnt = Counter()
        for i in nums:
            cnt[i] += 1
            if cnt[i] > 1 or i == "0":
                return False
        if len(cnt) != 9:
            return False
        return True
