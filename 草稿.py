nums = [1, 2, 3, 4]

a = [1]
n = len(nums)
b = nums.copy()
print(nums)
for i in range(1, n):
    a.append(a[i - 1] * nums[i - 1])
print(a)

res = 1
for j in range(n - 1, -1, -1):
    if j == n - 1:
        b[j] = res
    else:
        res *= nums[j + 1]
        b[j] = res

print(b)
for i in range(n):
    nums[i] = a[i] * b[i]
print(nums)
