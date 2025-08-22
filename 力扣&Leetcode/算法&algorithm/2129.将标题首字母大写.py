class Solution:
    def capitalizeTitle(self, title: str) -> str:
        # lower
        title = [i.lower() for i in title]
        res = "".join(title).split()
        ans = []
        for i in res:
            if len(i) > 2:
                a = i.title()
            else:
                a = i
            ans.append(a)
            ans.append(" ")
        del ans[-1]
        return "".join(ans)
