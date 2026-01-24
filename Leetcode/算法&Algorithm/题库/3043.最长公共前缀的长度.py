class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        cnt = set()
        for i in arr1:
            for j in range(1, len(str(i)) + 1):
                print(str(i)[:j])
                cnt.add(str(i)[:j])
        ans = 0
        for i in arr2:
            for j in range(1, len(str(i)) + 1):
                if str(i)[:j] in cnt:
                    ans = max(ans, len(str(i)[:j]))
        return ans
