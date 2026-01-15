import sys


def fun(a, b, s):
    nums = [int(i) if i in "01" else "X" for i in s]
    n = len(nums)
    l, r = 0, n - 1
    while l <= r:
        if nums[l] != "X" and nums[r] == "X":
            nums[r] = nums[l]
        elif nums[r] != "X" and nums[l] == "X":
            nums[l] = nums[r]
        elif nums[l] != "X" and nums[r] != "X" and nums[l] != nums[r]:
            return -1
        l += 1
        r -= 1
    rem_0 = a - nums.count(0)
    rem_1 = b - nums.count(1)
    if rem_0 < 0 or rem_1 < 0:
        return -1
    l, r = 0, n - 1
    while l <= r:
        if nums[l] == "X":
            if l == r:
                if rem_0 > 0:
                    nums[l] = 0
                    rem_0 -= 1
                elif rem_1 > 0:
                    nums[l] = 1
                    rem_1 -= 1
                else:
                    return -1
            else:
                if rem_0 >= 2:
                    nums[l] = nums[r] = 0
                    rem_0 -= 2
                elif rem_1 >= 2:
                    nums[l] = nums[r] = 1
                    rem_1 -= 2
                else:
                    return -1
        l += 1
        r -= 1
    if rem_0 == 0 and rem_1 == 0:
        return "".join(map(str, nums))
    return -1


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    s = input()
    print(fun(a, b, s))
