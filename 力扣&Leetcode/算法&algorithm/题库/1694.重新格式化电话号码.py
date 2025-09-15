class Solution:
    def reformatNumber(self, number: str) -> str:
        nums = [i for i in number if i.isdigit()]
        if len(nums) <= 3:
            return "".join(map(str, nums))
        if len(nums) % 3 == 1:
            p1 = nums[:-4]
            p2 = nums[-4:]
            aa = "".join(["-", p2[0], p2[1], "-", p2[2], p2[3]])
        elif len(nums) % 3 == 2:
            p1 = nums[:-2]
            p2 = nums[-2:]
            aa = "".join(["-", p2[0], p2[1]])
        elif len(nums) % 3 == 0:
            p1 = nums
            aa = ""
        res = deque(p1)
        ans = []
        while res:
            a = []
            for _ in range(3):
                if not res:
                    break
                cur = res.popleft()
                a += cur
            a += "-"
            ans += a
        ans1 = ""
        if ans != []:
            del ans[-1]
            ans1 = "".join(ans)
        else:
            aa = aa[1:]
        return ans1 + aa
