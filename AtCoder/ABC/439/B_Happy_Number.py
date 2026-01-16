import sys

input = sys.stdin.readline
n = int(input())


def fun(n):
        ans = 0
        for i in str(n):
            ans += int(i) ** 2
        return ans

cnt = set()
while n != 1 and n not in cnt:
    cnt.add(n)
    n = fun(n)
    
if n == 1:
    print("Yes")
else:
    print("No")
