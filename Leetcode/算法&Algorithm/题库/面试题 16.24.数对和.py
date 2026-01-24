class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        cnt = Counter()
        res = []
        for i in nums:
            tar = target - i
            if tar in cnt:
                res.append([tar, i])
                cnt[tar] -= 1
                if cnt[tar] == 0:
                    del cnt[tar]
            else:
                cnt[i] += 1
        return res
