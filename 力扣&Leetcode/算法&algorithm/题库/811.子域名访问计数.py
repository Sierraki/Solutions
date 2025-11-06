class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        def fun(tar=str):
            res = tar.split()
            p2 = res[-1].split(".")
            for i in range(len(p2)):
                cnt[".".join(p2[i:])] += int(res[0])

        cnt = Counter()
        for i in cpdomains:
            fun(i)
        ans = []
        for i, j in cnt.items():
            ans.append(f"{j} {i}")
        return ans
