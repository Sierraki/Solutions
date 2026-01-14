from collections import Counter
import sys
input=sys.stdin.readline
size=int(input())
for _ in range(size):
    n=int(input())
    s=input()
    cnt=Counter()
    for i,j in enumerate(s):
        if j not in cnt:
            cnt[j]=i
        else:
            if i-cnt[j]==1:
                cnt[j]+=1
            else:
                print('NO')
                break
    else:
        print('YES')