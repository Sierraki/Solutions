import sys


def fun(nums):
    odd = even = cnt = 0

    for i, j in enumerate(nums):
        if i % 2 != j % 2:
            cnt += 1
        if j % 2 == 0:
            even += 1
        else:
            odd += 1
    if even >= odd and even - odd <= 1:
        return cnt // 2
    return -1


n = int(input())
for _ in range(n):
    m = input()
    nums = list(map(int, input().split()))
    print(fun(nums))
