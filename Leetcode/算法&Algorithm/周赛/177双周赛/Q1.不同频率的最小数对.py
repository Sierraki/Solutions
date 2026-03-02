class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        res = list(set(nums))
        res.sort()
        ans = [float("inf"), float("inf")]
        for i in range(len(res) - 1):
            for j in range(i + 1, len(res)):
                a, b = res[i], res[j]
                if cnt[a] != cnt[b]:
                    if a <= ans[0]:
                        if b <= ans[1]:
                            ans = [a, b]
        if ans != [float("inf"), float("inf")]:
            return ans
        return [-1, -1]
