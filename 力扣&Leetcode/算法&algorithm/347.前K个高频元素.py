class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        res = [[i, j] for i, j in cnt.items()]
        res.sort(key=lambda x: x[1], reverse=True)
        ans = []
        for i in range(k):
            if i < len(res):
                ans.append(res[i][0])
        return ans
