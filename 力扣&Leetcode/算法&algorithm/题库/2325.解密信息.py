class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        al = "abcdefghijklmnopqrstuvwxyz"
        res = []
        for i in key:
            if i not in res and i != " ":
                res.append(i)
        res = "".join(res)
        a = dict(zip(res, al))
        a[" "] = " "
        ans = []
        for i in message:
            ans.append(a[i])
        return "".join(ans)
