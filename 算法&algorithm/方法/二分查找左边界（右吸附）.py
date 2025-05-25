nums = [0, 1, 1, 1, 2, 2, 3, 3, 5]
arrr = [0, 1, 2, 3, 4, 5, 6, 7, 8]

target = 0.5

left, right = 0, len(nums) - 1
ans = -1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] >= target:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
