import sys

input = sys.stdin.readline
n = int(input())
c = [0] * (n + 1)
x = 1
while x * x <= n:
    y = x + 1
    while True:
        val = x * x + y * y
        if val > n:
            break
        c[val] += 1
        y += 1
    x += 1
ans = []
for n in range(1, n + 1):
    if c[n] == 1:
        ans.append(n)
print(len(ans))
if ans:
    print(" ".join(map(str, ans)))
