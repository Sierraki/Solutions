nums = [int(i) for i in input().split()]
nums.sort()
if nums[-1] - nums[0] >= 10:
    print("check again")
else:
    print("final " + str(nums[1]))
