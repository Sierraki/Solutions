class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        ans = [""]
        for i in arr:
            if cnt[i] == 1:
                ans.append(i)
        if k >= len(ans):
            return ans[0]
        return ans[k]
