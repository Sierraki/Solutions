class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        cnt1 = Counter()
        cnt2 = Counter()
        for idx, i in enumerate(list1):
            if i not in cnt1:
                cnt1[i] = idx
        for idx, i in enumerate(list2):
            if i not in cnt2:
                cnt2[i] = idx
        res = list(set(list1 + list2))
        ans = Counter()
        for i in res:
            if i in cnt1 and i in cnt2:
                ans[i] = cnt1[i] + cnt2[i]
        tar = min(ans.values())
        ans1 = []
        for i, j in ans.items():
            if j == tar:
                ans1.append(i)
        return ans1
