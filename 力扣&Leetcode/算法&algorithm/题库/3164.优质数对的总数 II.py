class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 算因子
        def fun(tar=int):
            for i in range(1, floor(sqrt(tar)) + 1):
                if tar % i == 0:
                    if tar // i == i:
                        cnt[i] -= 1
                    cnt[i] += 1
                    cnt[tar // i] += 1

        cnt = Counter()
        for i in nums1:
            fun(i)
        ans = 0
        for i in nums2:
            if i * k in cnt:
                ans += cnt[i * k]
        return ans
