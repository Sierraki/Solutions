class Solution:
    def calculate(self, s: str) -> int:
        res = [i for i in s if i != " "]
        nums = []
        pin = 0
        for i in range(len(res)):
            if res[i] in "+-*/":
                nums.append("".join(res[pin:i]))
                nums.append(res[i])
                pin = i + 1
            if i == len(res) - 1 and res[i].isdigit():
                nums.append("".join(res[pin:]))
        ans = []
        res = deque(nums)
        while res:
            if res[0].isdigit():
                ans.append(int(res[0]))
            else:
                cur = res.popleft()
                if cur == "+":
                    ans.append(int(res[0]))
                elif cur == "-":
                    ans.append(int("-" + res[0]))
                elif cur == "*":
                    ans[-1] = int(ans[-1]) * int(res[0])
                elif cur == "/":
                    ans[-1] = int(ans[-1]) / int(res[0])
            res.popleft()
        return sum(map(int, ans))
