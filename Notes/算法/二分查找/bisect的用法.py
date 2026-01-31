from bisect import bisect_left, bisect_right

# 对于存在数字,bisect_left是插到存在数字的第一位,bisect_right是插到最后一位+1

nums = [10, 20, 20, 20]

print(bisect_left(nums, 20))  # 1
print(bisect_right(nums, 20))  # 4

# 对于不存在数字，都指向应该插入的位置

print(bisect_left(nums, 15))  # 1
print(bisect_right(nums, 15))  # 1
