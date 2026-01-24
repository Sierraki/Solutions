import sys

input = sys.stdin.readline

a =  input() 
b =  input() 
n=len(a)

for  i in range(n):
    if a[i].lower()==b[i].lower():
        continue
    else:
        if a[i].lower()<b[i].lower():
            print(-1)
            break
        else:
            print(1)
            break
else:
    print(0)