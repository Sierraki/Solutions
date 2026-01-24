class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(list)
        for i, j in enumerate(nums):
            cnt[j].append(i)
        ans = 0
        for i, j in enumerate(nums):
            if j != "x":
                tar = k - j
                if tar in cnt:
                    nums[i] = "x"
                    nums[cnt[tar][-1]] = "x"
                    cnt[tar].pop()
                    if len(cnt[j]) >= 1:
                        cnt[j].pop()
                        ans += 1
                    if not cnt[tar]:
                        del cnt[tar]
                    if not cnt[j]:
                        del cnt[j]
        return ans
