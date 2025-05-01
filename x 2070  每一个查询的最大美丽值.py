items =[[1,2]]
queries = [[1,2]]
items.sort()

n=len(items)
a=[0]*(len(queries))

for  idx,i in enumerate(queries):
    left=0
    right=n-1
    target=i
    cur=big=0
    while left<right:
        mid=(left+right)//2
        if target>items[-1][0]:
            # print(target)
            a[idx]=target
            break
        # print(items[mid],left,mid,right)
        if target==items[-1][0]:
            a[idx]=items[-1][-1]
            break
        if left==mid:
            # print(items[mid])
            
            for j in range(mid+1):
                cur=items[j][-1]
                big=max(cur,big)
            # print(big)
            a[idx]=big
            break
        if target>=items[mid][0]:
            left=mid
        else:
            right=mid
print(a)

        
    
    



