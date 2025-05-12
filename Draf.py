from collections import Counter

num1 = 1
num2 = 10
num3 = 100

nums = [str(num1), str(num2), str(num3)]
for i in range(len(nums)):
    nums[i] = nums[i].zfill(4)
print(nums)
a = []
for i in range(len(nums[0])):
    mi = 9
    for j in nums:
        mi = min(mi, int(j[i]))
    a.append(mi)

print(a)
b = "".join(map(str, a))
print(int(b))
