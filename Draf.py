from math import ceil, sqrt
from operator import le
from turtle import left


nums = [5, 2, 8, 1, 9, 4, 7, 3, 6, 2]

n = len(nums)
n1 = int(n**0.5)
block = []
for i in range(0, n, n1):
    block.append(sum(nums[i:i + n1]))
print(block)


def ask(left, right):
    ans = 0
    b1 = left // n1
    b2 = right // n1
    if b1 == b2:
        return sum(nums[left: right + 1])
    ans = sum(nums[left: (b1 + 1) * n1])
    ans += sum(block[b1 + 1: b2])
    ans += sum(nums[b2 * n1: right + 1])
    return ans

def update(idx, val):

    lc = (idx) // n1
    block[lc] = block[lc] - nums[idx] + val
    nums[idx] = val


print(ask(2, 7))
# update(4, 5)
# print(ask(1, 8))

# update(0, 10)
# print(ask(0, 3))
