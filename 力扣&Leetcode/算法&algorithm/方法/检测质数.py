n = 4

# 普通
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
# 埃氏筛
mx=10**6#范围
# 找出范围内的质数，大范围搜索
primes=[]
res=[True]*mx

for i in range(2,mx+1):
    # 对每个res的值遍历，True表示为质数
    if res[i]:
        primes.append(i)
        # 如果是，就加入primes
        for j in range(i*i ,mx,i):
            # 证明，res[i]的倍数的数不是质数，所以步差为i
            res[j]=False

