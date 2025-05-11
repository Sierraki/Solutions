from collections import Counter

s = "aaaabbbbcccc"
cnt = Counter(s)
print(cnt)
a = [i for i in cnt]
print(a)
k = len(cnt)
n = len(s)
print(n, k)
a1 = sorted(a)
a2 = sorted(a, reverse=True)
print(a1, a2)
a=a1+a2
b = a * int(n / k/2)
b = "".join(b)
print(b)
