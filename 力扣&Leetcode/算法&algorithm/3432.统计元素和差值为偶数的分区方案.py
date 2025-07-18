class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        p = []
        s = 0
        for i in nums:
            s += i
            p.append(s)
        ans = 0
        for i in range(len(nums) - 1):
            if (2 * p[i] - p[-1]) % 2 == 0:
                print(i)
                ans += 1
        return ans
