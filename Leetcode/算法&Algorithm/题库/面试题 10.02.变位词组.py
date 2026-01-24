class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = defaultdict(list)

        def fun(nums):
            nums = [i for i in nums]
            nums.sort()
            return "".join(nums)

        for i in strs:
            cnt[fun(i)].append(i)
        return [i for i in cnt.values()]
