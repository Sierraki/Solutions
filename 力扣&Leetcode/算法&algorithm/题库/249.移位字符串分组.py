class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        cnt = defaultdict(list)

        def fun(tar):
            if len(tar) == 1:
                return "x"
            ans = ""
            for i in range(1, len(tar)):

                if ord(tar[i]) - ord(tar[i - 1]) > 0:
                    ans += str(ord(tar[i]) - ord(tar[i - 1])) + "/"
                else:
                    ans += str(ord(tar[i]) - ord(tar[i - 1]) + 26) + "/"
            return ans

        for i in strings:
            cnt[fun(i)].append(i)
        return [i for i in cnt.values()]
