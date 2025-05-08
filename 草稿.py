from collections import Counter
import bisect


queries = ["cbd"]
words = ["zaaaz"]
for idx, i in enumerate(words):
    a = Counter(i)
    words[idx] = a[min(a)]

for idx, i in enumerate(queries):
    a = Counter(i)
    queries[idx] = a[min(a)]

words.sort()
print(words)
print(queries)
n = len(words)

for idx, i in enumerate(queries):
    lc = bisect.bisect(words, i)
    queries[idx] = n - lc

print(queries)
