n = 100007

st = True
if n <= 1:
    st = False
elif n == 2:
    st = True
else:
    for i in range(3, int(n**0.05) + 1, 2):
        if n % i == 0:
            st = False
print(st)
