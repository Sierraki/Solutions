n = 4

st = True
if n <= 1:
    st = False
elif n == 2:
    st = True
elif n % 2 == 0:
    st=False
else:
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            st = False
print(st)
