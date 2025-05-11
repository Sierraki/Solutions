s = "abc"
t = "bac"

cur = 0
for idx, i in enumerate(s):

    lc = t.index(i)
    print(idx, lc)
    cur += abs(idx - lc)
print(cur)
