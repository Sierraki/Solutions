class Solution:
    def calculate(self, s: str) -> int:
        # 处理字符串，分割符号
        s = [i for i in s if i != " "]
        s = "".join(s)
        nums = []
        pin = 0
        for i, j in enumerate(s):
            if j.isdigit():
                continue
            else:
                nums.append(s[pin:i])
                nums.append(j)
                pin = i + 1
        if s[pin].isdigit():
            nums.append(s[pin:])
        ans = []
        nums = deque(nums)
        while nums:
            if nums[0].isdigit():
                ans.append(int(nums[0]))
                nums.popleft()
            else:
                cur = nums.popleft()
                if cur == "+":
                    ans.append(int(nums[0]))
                elif cur == "-":
                    ans.append(int("-" + nums[0]))
                elif cur == "*":
                    ans[-1] = ans[-1] * int(nums[0])
                else:
                    ans[-1] = int(ans[-1] / int(nums[0]))
                nums.popleft()
        return int(sum(ans))
