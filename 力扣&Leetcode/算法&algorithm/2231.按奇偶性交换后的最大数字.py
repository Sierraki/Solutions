class Solution:
    def largestInteger(self, num: int) -> int:
        n = len(str(num))
        res = [0] * n
        odd = []
        even = []
        o = e = 0
        for idx, i in enumerate(str(num)):
            if int(i) % 2 == 0:
                even.append(int(i))
                res[idx] = 0
            else:
                odd.append(int(i))
                res[idx] = 1
        even.sort(reverse=True)
        odd.sort(reverse=True)
        for i in range(len(res)):
            if res[i] == 0:
                res[i] = even[e]
                e += 1
            else:
                res[i] = odd[o]
                o += 1
        ans = "".join(map(str, res))
        return int(ans)
