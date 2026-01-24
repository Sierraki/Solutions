class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nums = [i for i in str(num)]
        n = len(nums)
        cnt = 0
        for i in range(n - k + 1):
            a = "".join(nums[i : i + k])

            if int(a) != 0 and num % int(a) == 0:
                cnt += 1

        return cnt
