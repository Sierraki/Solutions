class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = 0

        def fun(a: str) -> str:
            if a == "X":
                return "0"
            else:
                return "X"

        nums = [i for i in s]
        for idx, i in enumerate(nums):
            if i == "X":
                nums[idx] = fun(i)
                if idx + 1 < len(nums):
                    nums[idx + 1] = fun(i)
                if idx + 2 < len(nums):
                    nums[idx + 2] = fun(i)
                ans += 1
        return ans
