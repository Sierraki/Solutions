from typing import List
from collections import defaultdict


class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mo = 10**9 + 7
        cnt = defaultdict(list)
        for i in range(k):
            if nums[i] not in cnt:
                cnt[nums[i]] = [nums[i]]
            else:
                cnt[nums[i]].append(nums[i] * cnt[nums[i]][-1])
        res = sum(i[-1] for i in cnt.values())
        cur = mx = res % mo
        for i in range(k, n):
            # 受影响的数，是nums[i],nums[i-k]
            if nums[i] == nums[i - k]:
                continue
            else:
                # REMOVE
                res -= cnt[nums[i - k]][-1]
                cnt[nums[i - k]].pop()
                if cnt[nums[i - k]] == []:
                    del cnt[nums[i - k]]
                else:
                    res += cnt[nums[i - k]][-1]
                # add
                if nums[i] in cnt:
                    res -= cnt[nums[i]][-1]
                    cnt[nums[i]].append(nums[i] * cnt[nums[i]][-1])
                else:
                    cnt[nums[i]] = [nums[i]]
                res += cnt[nums[i]][-1]
                cur = res % mo
                mx = max(cur, mx)
                # print(cur, mx)
        return mx


example = Solution()
print(example.maxFrequencyScore([1, 1, 1, 2, 1, 2], 3))  # 5
print(example.maxFrequencyScore([1, 1, 1, 1, 1, 1], 4))  # 1
