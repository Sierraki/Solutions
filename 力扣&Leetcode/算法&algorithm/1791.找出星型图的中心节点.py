class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        cnt = Counter()
        for i, j in edges:
            cnt[i] += 1
            cnt[j] += 1
        ans = max(cnt, key=lambda x: cnt[x])
        return ans
