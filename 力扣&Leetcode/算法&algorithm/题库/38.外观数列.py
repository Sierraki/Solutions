class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        nums = "1"

        def fun1(nums):
            pin = 0
            ans = []
            for i in range(len(nums)):
                if nums[i] != nums[pin]:
                    ans.append(nums[pin:i])
                    pin = i
            ans.append(nums[pin:])
            return ans

        def fun2(res):
            ans = ""
            for i in res:
                ans += str(len(i)) + i[0]
            return ans

        for _ in range(n - 1 - 1):
            nums = fun1(fun2(nums))
        return fun2(nums)
