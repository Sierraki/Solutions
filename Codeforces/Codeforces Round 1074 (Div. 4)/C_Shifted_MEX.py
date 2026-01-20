import sys

input = sys.stdin.readline

size = int(input())
for _ in range(size):
    n = int(input())
    nums = sorted(list(set(map(int, input().split()))))
    cnt=mx=1
    if n>1:
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                cnt+=1
                mx=max(mx,cnt)
            else:
                cnt=1
    print(mx)    
