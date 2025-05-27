nums=[2,0,2,1,1,0]
left = i = 0
right = len(nums) - 1

# [0,left)为 0 区间
# [left,i)为 1 区间
# (right,n-1]为 2 区间

while i <= right:
    if nums[i] == 0:
        nums[left], nums[i] = nums[i], nums[left]
        left += 1
        i += 1
    elif nums[i] == 2:
        nums[i], nums[right] = nums[right], nums[i]
        right -= 1
    else:
        i += 1

print(nums)