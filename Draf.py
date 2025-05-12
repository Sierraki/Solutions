tickets = [2, 3, 2]
k = 2

cnt = 0
while tickets[k] > 0:
    for i in range(len(tickets)):
        if tickets[i]>0:
            tickets[i]-=1
            cnt+=1
print(cnt)
