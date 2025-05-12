from collections import defaultdict

items1 = [[1, 1], [4, 5], [3, 8]]
items2 = [[3, 1], [1, 5]]

cnt = defaultdict()
items1 += items2
for i in items1:
    if i[0] not in cnt:
        cnt[i[0]] = 0
print(cnt)
for i in items1:
    cnt[i[0]] += i[1]
print(cnt)
a = [[i, j] for i, j in cnt.items()]
a.sort()
print(a)
