class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        mod = 10**9 + 7

        odd = defaultdict(int)
        even = defaultdict(int)

        cur = 0
        ans = 0
        n = len(nums)

        for i in range(n):
            cur ^= nums[i]
            ocur = 1 if cur == target1 else 0
            ocur = ocur + even[cur ^ target1]

            ecur = odd[cur ^ target2]
            if i == n - 1:
                ans = (ocur + ecur) % mod
            odd[cur] = odd[cur] + ocur
            even[cur] = even[cur] + ecur

        return ans
