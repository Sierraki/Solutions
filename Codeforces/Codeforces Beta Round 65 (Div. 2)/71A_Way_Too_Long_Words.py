n = int(input())
for _ in range(n):
    a = input()
    if len(a) <= 10:
        print(a)
    else:
        print(f"{a[0]}{len(a)-2}{a[-1]}")
