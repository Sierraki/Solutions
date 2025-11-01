n = int(input())
for _ in range(n):
    le = input()
    res = input().split()
    print(len(set(res)) * 2 - 1)
