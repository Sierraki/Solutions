class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1", "8"]
        tar = n // 2
        nums = [0, 6, 1, 9, 8] * tar
        res = set()

        def bt(start, cur):
            if len(cur) == tar:
                ans = "".join(map(str, cur))
                if len(str(int(ans))) == tar and ans != "0":
                    res.add(ans)
                return
            for i in range(start, len(nums)):
                cur.append(nums[i])
                bt(i + 1, cur)
                cur.pop()

        bt(0, [])
        cnt = {"0": "0", "9": "6", "6": "9", "1": "1", "8": "8"}
        res1 = []

        def fun(tar):
            ans = ""
            for i in range(len(tar) - 1, -1, -1):
                ans += cnt[tar[i]]
            if n % 2 == 1:
                for j in ["1", "0", "8"]:
                    res1.append(tar + j + ans)
            else:
                res1.append(tar + ans)

        for i in res:
            fun(i)
        return res1
