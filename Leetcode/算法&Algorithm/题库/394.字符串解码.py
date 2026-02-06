class Solution:
    def decodeString(self, s: str) -> str:
        nums = deque(list(s))
        res = []
        while nums:
            cur = ""
            while nums[0].isdigit():
                cur += nums.popleft()
            if cur.isdigit():
                left = 0
                right = 0
                tmp = []
                while left == right == 0 or left != right:
                    curr = nums.popleft()
                    if curr == "[":
                        left += 1
                    if curr == "]":
                        right += 1
                    tmp.append(curr)
                for _ in range(int(cur)):
                    nums.extendleft(reversed(tmp[1:-1]))
            else:
                res.append(nums.popleft())
        ans = ""
        for i in res:
            if i not in "[]":
                ans += i
        return ans
