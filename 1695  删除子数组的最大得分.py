class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cnt=defaultdict(int)
        n=len(nums)

        left=cur=big=0

        for  i in range(n):
            cnt[nums[i]]+=1
            cur+=nums[i]
            if cnt[nums[i]]>1:
                while cnt[nums[i]]>1:
                    cnt[nums[left]]-=1
                    cur-=nums[left]
                    left+=1
         
            big=max(cur,big)
        
        return(big)