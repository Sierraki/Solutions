from collections import defaultdict
class Solution:
    def findSpecialInteger(self, arr) -> int:
        n=len(arr)
        k=int(n//4)
        cnt=defaultdict(int)
        for i in arr:
            cnt[i]+=1
            if cnt[i]>k:
                return i

sol=Solution()
print(sol.findSpecialInteger([1,2,2,6,6,6,6,7,10]))