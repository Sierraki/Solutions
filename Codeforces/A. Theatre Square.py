def solve():
    m, n, a = map(int, input().split())
    aa = (m + a - 1) // a
    bb = (n + a - 1) // a
    return aa * bb


print(solve())
