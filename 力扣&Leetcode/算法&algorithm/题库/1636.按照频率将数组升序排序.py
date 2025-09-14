class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        res = [[i, j] for i, j in cnt.items()]
        res.sort(key=lambda x: (x[1], -x[0]))
        ans = []
        for i in range(len(res)):
            ans += [res[i][0]] * res[i][1]
        return ans
