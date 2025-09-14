class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        cnt = Counter()
        ans = 0
        for i in range(len(arrivals)):
            if i >= w:
                if arrivals[i - w] > 0:
                    cnt[arrivals[i - w]] -= 1
            if arrivals[i] > 0 and cnt[arrivals[i]] + 1 > m:
                arrivals[i] = 0
                ans += 1
            else:
                cnt[arrivals[i]] += 1
        return ans
