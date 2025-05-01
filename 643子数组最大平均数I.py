class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)


        big=sum(nums[:k])

        cur=sum(nums[:k])

        for i in range(1,n-k+1):
            cur=cur+nums[i+k-1]-nums[i-1]
            
            if cur >= big:
                big = cur

        if k>n:
            return big/n
        else:
            return big/k
            
