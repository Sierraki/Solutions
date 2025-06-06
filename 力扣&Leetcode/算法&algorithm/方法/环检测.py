source = [1, 2, 3, 4, 5]
target = [3, 4, 5, 1, 2]

# 对source遍历
# 同个位置上不同的打tag
# 建立source字典，val：idx

map1 = {i: idx for idx, i in enumerate(source)}
print(map1)
check = [False] * len(source)
tcnt = 0
print(source)
print(target)
for idx, i in enumerate(source):
    cnt = 0
    if not check[idx]:
        # 指针指向当前位置，检测当前位置是不是true
        # 是true跳过，不是就继续
        # 不是的话，给指针位置打tag
        # 找出要换的数字在source中的位置lc
        # 对换当前lc和pin位置，pin挪到lc，继续
        pin = idx
        while (
            check[pin] == False
            and source[map1[target[pin]]] != target[map1[target[pin]]]
        ):
            check[pin] = True
            lc = map1[target[pin]]

            source[pin], source[lc] = source[lc], source[pin]
            pin = lc
            cnt += 1
        tcnt += cnt
print(tcnt)
