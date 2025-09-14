class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        # check code
        def fun(x: str) -> bool:
            if not x:
                return False
            for i in x:
                if not (i.isalpha() or i.isdigit() or i == "_"):
                    return False
            return True

        cnt = {"electronics": [], "grocery": [], "pharmacy": [], "restaurant": []}
        for i in range(len(code)):
            if fun(code[i]) and isActive[i] and businessLine[i] in cnt:
                cnt[businessLine[i]].append(code[i])
        ans = []
        for i in cnt.values():
            if i != []:
                ans += sorted(i)
        return ans
