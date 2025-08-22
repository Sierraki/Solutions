class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        nums = [i for i in range(1, n + 1)]
        res = deque(nums)
        cnt = Counter(nums)
        cnt[1] += 1
        t = 0
        cnt = Counter(nums)
        while max(cnt.values()) < 3:
            res.rotate(-t * k)
            cnt[res[0]] += 1
            t += 1
        ans = [i for i, j in cnt.items() if j == 1]
        return ans
