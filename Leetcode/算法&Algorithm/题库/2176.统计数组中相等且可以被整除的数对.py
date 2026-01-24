class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(list)
        for idx, val in enumerate(nums):
            cnt[val].append(idx)
        ans = 0
        for idxs in cnt.values():
            n = len(idxs)
            for i in range(n):
                for j in range(i + 1, n):
                    if (idxs[i] * idxs[j]) % k == 0:
                        ans += 1
        return ans
