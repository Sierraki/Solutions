class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        ans = []
        mi = 0
        mx = n
        # I add mi
        # D add mx
        for i in s:
            if i == "D":
                ans.append(mx)
                mx -= 1
            else:
                ans.append(mi)
                mi += 1
        ans.append(mi)
        print(ans)
        return ans
