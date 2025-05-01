s = "111000"

s=[int(i) for i in s]
s+=s
n=len(s)
k=int(n/2)

for i in range(n):
    if s[i]==0:
        s[i]-=1
        
cur=mi=sum(s[:k])




print(cur)
print(s)