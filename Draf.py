from collections import Counter, defaultdict
import bisect

nums = [4,5,6,7,0,1,2]
target = 0

left,right=0,len(nums)-1

while left<right:
    mid=(right+left)//2
    if nums[mid]>nums[right]:
        left=mid+1
    elif nums[mid]<nums[right]:
        right=mid
    else:
        right-=1
print(left)
if n