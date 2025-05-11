import string

target = 18

nums = [i for i in range(target)]
print(nums)

left,right=0,1
cur=nums[left]
while right<target:
    cur+=nums[right]
    while cur!=target<18