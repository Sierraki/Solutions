class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        tar = set()
        ans = 0
        for i, j in cnt.items():
            if j > 1:
                tar.add(i)
        if not tar:
            return 0
        else:
            pin = 2
            n = len(nums)
            while pin < n:
                cur = nums[pin - 2 : pin + 1]
                for i in cur:
                    cnt[i] -= 1
                    if cnt[i] <= 1:
                        if i in tar:
                            tar.remove(i)
                ans += 1
                if not tar:
                    return ans
                pin += 3
            if max(cnt.values()) > 1:
                return ans + 1
            return ans
