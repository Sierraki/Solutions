class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        cur = left = 0
        s = n
        cnt = 0

        if sum(nums) < target:
            return 0
        else:
            for i in range(n):
                cur += nums[i]
                cnt += 1
                if cur < target:

                    continue
                else:
                    while cur >= target:
                        if cur >= target:
                            s = min(cnt, s)

                        cur -= nums[left]

                        left += 1
                        cnt -= 1

            return s
