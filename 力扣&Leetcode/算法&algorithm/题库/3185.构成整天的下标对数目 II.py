class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = Counter()
        for i in hours:
            if i % 24 == 0:
                cnt[0] += 1
            else:
                cnt[i % 24] += 1
        ans = 0
        check = Counter()
        for i, j in cnt.items():
            if i == 0:
                ans += (j - 1) * j // 2
            else:
                tar = 24 - i
                if tar == i:
                    ans += (j - 1) * j // 2
                else:
                    if tar in cnt and tar not in check:
                        ans += j * cnt[tar]
                        check[i] += 1
        return ans
