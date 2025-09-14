class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = defaultdict(list)

        def fun(a=str):
            return "".join(sorted([i for i in a]))

        for i in strs:
            res = fun(i)
            cnt[res].append(i)
        return [i for i in cnt.values()]
