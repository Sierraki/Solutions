class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for i in range(5):
            if 0 <= i <= 4 and 0 <= turnedOn - i <= 59:
                res.append([i, turnedOn - i])
        cnt = defaultdict(list)
        for i in range(60):
            cnt[bin(i)[2:].count("1")].append(str(i).zfill(2))
        def fun(a=int, b=int):
            hour = [i for i in cnt[a] if int(i) <= 11]
            mins = [i for i in cnt[b] if int(i) <= 59]
            ans = []
            for i in range(len(hour)):
                for j in range(len(mins)):
                    ans.append(f"{int(hour[i])}:{mins[j]}")
            return ans
        ans = []
        for i in res:
            ans += fun(i[0], i[1])
        return ans