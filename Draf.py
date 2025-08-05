from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List

s = "aabaabaaf"
word = "aabaaf"  b

lps = [0] * len(word)
mx = 0
for i in range(1, len(word)):
    while mx > 0 and word[i] != word[mx]:
        mx = lps[mx - 1]
    if word[i] == word[mx]:
        mx += 1
    lps[i] = mx
tar = [0, 1, 0, 1, 2, 0]
print(lps)

i = j = 0

while i < len(s):

    if s[i] == word[j]:
        j += 1
        i += 1
    
    if j == len(word):
            print(True)
            break
    elif i <len(s) and s[i]!=word[j]:
        if j!=0:
            j=lps[j-1]
        else:
            i+=1

print(False)
