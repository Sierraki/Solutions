class Solution:
    def simplifyPath(self, path: str) -> str:
        res = path.split("/")
        ans = []
        while res:
            if (
                res[0] == ""
                or res[0] == "."
                or (res[0][0] == "." and len(res[0]) > 3 and set(res[0]) == 1)
            ):
                del res[0]
            elif res[0] == "..":
                if ans != []:
                    ans.pop()
                del res[0]
            else:
                ans.append(res[0])
                del res[0]
        return "/" + "/".join(ans)
